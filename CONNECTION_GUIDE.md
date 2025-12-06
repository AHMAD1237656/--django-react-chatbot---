# Connection Fix Guide 🔧

## Server Connection Issues - SOLVED ✅

### What Was Fixed:
1. ✅ **CORS Configuration** - Added explicit localhost:3000 to allowed origins
2. ✅ **Error Handling** - Better error messages when connection fails
3. ✅ **Settings Reloaded** - Django server now recognizes React on port 3000

---

## How to Run Your Chatbot:

### Step 1: Start Django Backend
```powershell
cd "C:\Users\hp\OneDrive\Desktop\Django Advance Course\django-react-chatbot\backend"
python manage.py runserver
```
✅ Server will run on: **http://localhost:8000**

### Step 2: Start React Frontend (NEW TERMINAL)
```powershell
cd "C:\Users\hp\OneDrive\Desktop\Django Advance Course\django-react-chatbot\frontend"
npm start
```
✅ App will run on: **http://localhost:3000**

---

## Testing the Connection:

### Open React App in Browser:
- Go to: **http://localhost:3000**
- You should see: "My Chatbot" with a chat box

### When You Send a Message:
1. Type any message in the input box
2. Press **Enter** or click **Send**
3. Message appears in blue (user)
4. Bot responds in green
5. Check browser console (F12) for debug messages

---

## If Connection Still Fails:

### ✅ Check 1: Is Backend Running?
```powershell
Invoke-WebRequest http://localhost:8000/api/conversations/ -Method POST -ContentType "application/json" -Body "{}"
```
If you get a response with `id`, backend is working ✅

### ✅ Check 2: Is Frontend Connected?
Open browser console (F12) and look for:
- ✅ "Conversation created: 1" = Connection OK
- ❌ "Failed to create conversation" = Check backend

### ✅ Check 3: Restart Everything
```powershell
# Kill all Python processes
Get-Process python -ErrorAction SilentlyContinue | Stop-Process -Force

# Restart backend
cd backend
python manage.py runserver

# In new terminal, restart frontend
cd frontend
npm start
```

---

## Configuration Details:

### Django Settings (backend/backend/settings.py):
- **DEBUG** = True ✅
- **ALLOWED_HOSTS** = ['*'] ✅
- **CORS_ALLOWED_ORIGINS** includes localhost:3000 ✅
- **corsheaders middleware** is enabled ✅

### React Setup (frontend/src/CHATBOX.js):
- Backend URL: `http://localhost:8000/api/`
- Auto-creates conversation on load
- Sends messages to `/api/messages/`
- Better error alerts if connection fails

---

## API Endpoints:

| Endpoint | Method | Purpose |
|----------|--------|---------|
| `/api/conversations/` | POST | Create new chat session |
| `/api/conversations/` | GET | List all conversations |
| `/api/messages/` | POST | Send/receive messages |
| `/api/messages/` | GET | Get messages for conversation |

---

## Common Issues & Solutions:

| Issue | Solution |
|-------|----------|
| "Cannot connect to server" | Make sure Django is running on port 8000 |
| CORS error in console | Django settings already fixed, just restart both apps |
| Message doesn't send | Check browser console for HTTP error code |
| "Bot is thinking..." stuck | Check backend console for AI service errors |

---

Generated: December 6, 2025 ✨
