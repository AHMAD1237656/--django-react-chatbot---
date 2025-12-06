from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from .models import Conversation, Message
from .serializers import ConversationSerializer, MessageSerializer
from .ai_service import get_ai_response

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 100
    page_size_query_param = 'page_size'
    max_page_size = 1000

class ConversationViewSet(viewsets.ModelViewSet):
    queryset = Conversation.objects.all()
    serializer_class = ConversationSerializer

class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all().order_by('created_at')  # ✅ Order by creation time
    serializer_class = MessageSerializer
    pagination_class = StandardResultsSetPagination

    def create(self, request, *args, **kwargs):
        try:
            data = request.data.copy()

            # ✅ Step A: Resolve or create conversation
            conv_id = data.get('conversation')
            conversation = None

            if conv_id:
                # Try to load existing conversation
                try:
                    conversation = Conversation.objects.get(id=conv_id)
                except Conversation.DoesNotExist:
                    # If invalid ID provided, create new conversation
                    conversation = Conversation.objects.create()
            else:
                # If not provided, create new conversation
                conversation = Conversation.objects.create()

            # Force the conversation ID into incoming data
            data['conversation'] = conversation.id

            # ✅ Step B: Validate and save user message
            serializer = self.get_serializer(data=data)
            serializer.is_valid(raise_exception=True)
            message = serializer.save()  # user message saved

            # ✅ Step C: If sender is user, create AI reply
            if message.sender == "user":
                try:
                    ai_text = get_ai_response(message.text)
                    print(f"✅ AI Response Generated: {ai_text[:50]}...")
                except Exception as e:
                    # If AI call fails, still return user message cleanly
                    print(f"❌ AI Error: {e}")
                    ai_text = "Sorry, I couldn't generate a response right now."

                bot_msg = Message.objects.create(
                    conversation=conversation,
                    sender="bot",
                    text=ai_text
                )
                print(f"✅ Bot Message Created: ID={bot_msg.id}")

            # ✅ Step D: Return user message payload
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

        except Exception as e:
            print("❌ Error in MessageViewSet.create:", e)
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)