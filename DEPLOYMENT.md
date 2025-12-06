# Django React Chatbot - Deployment Guide

## Deploy on Render.com (Free)

### Step 1: Push to GitHub
```bash
git add .
git commit -m "Add deployment configuration"
git push
```

### Step 2: Create Render Account
1. Go to [Render.com](https://render.com)
2. Sign up with GitHub

### Step 3: Deploy the App
1. Click **"New +"** → **"Web Service"**
2. Select your GitHub repository: `--django-react-chatbot---`
3. Fill in these details:
   - **Name**: `django-react-chatbot`
   - **Environment**: `Python 3`
   - **Build Command**: `pip install -r requirements.txt && cd frontend && npm install && npm run build`
   - **Start Command**: `gunicorn backend.wsgi`
   - **Plan**: Free

4. Click **"Create Web Service"**

### Step 4: Add Environment Variables
In Render dashboard:
- `DEBUG`: `false`
- `SECRET_KEY`: (Auto-generated)
- `ALLOWED_HOSTS`: Your Render URL

### Step 5: Wait for Deployment
- Takes 3-5 minutes
- You'll get a live URL like: `https://django-react-chatbot.onrender.com`

## Deploy on Vercel (Alternative)
- Frontend: Deploy on Vercel
- Backend: Deploy on Render or Railway

## Local Testing Before Deploy
```bash
# Backend
cd backend
python manage.py runserver

# Frontend (new terminal)
cd frontend
npm start
```

---
**Repository**: https://github.com/AHMAD1237656/--django-react-chatbot---
