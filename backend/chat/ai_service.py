from openai import OpenAI
from django.conf import settings
import os

def get_ai_response(user_message):
    """Get AI response from OpenAI API or fallback to mock"""
    try:
        # Try to get API key from settings or environment
        api_key = getattr(settings, 'OPENAI_API_KEY', None) or os.getenv('OPENAI_API_KEY')
        
        if not api_key:
            # Fallback: Provide smart responses without API key
            user_lower = user_message.lower()
            
            # Simple response mapping for demo
            if "hello" in user_lower or "hi" in user_lower:
                return "Hello! 👋 I'm a chatbot. How can I help you today?"
            elif "how are you" in user_lower:
                return "I'm doing great! Thanks for asking. How can I assist you?"
            elif "what is" in user_lower or "who is" in user_lower:
                return f"That's an interesting question about '{user_message}'. I'd need an OpenAI API key to provide detailed answers."
            elif "bye" in user_lower or "goodbye" in user_lower:
                return "Goodbye! Have a great day! 👋"
            else:
                return f"I received your message: '{user_message}'. To enable AI responses, please configure your OpenAI API key."
        
        # ✅ Use the modern OpenAI client format
        client = OpenAI(api_key=api_key)
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": user_message}
            ],
            max_tokens=150,
            temperature=0.7
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        print(f"❌ AI Error: {e}")
        return f"Sorry, I encountered an error: {str(e)[:100]}"