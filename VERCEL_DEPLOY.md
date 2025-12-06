## 🚀 VERCEL DEPLOYMENT GUIDE

### For Frontend Only (React on Vercel)

1. **Go to https://vercel.com**
2. **Sign up with GitHub**
3. **Import Project** → Select `--django-react-chatbot---`
4. **Configure:**
   - Framework: React
   - Root Directory: `frontend`
   - Build Command: `npm run build`
   - Output Directory: `build`

5. **Add Environment Variables:**
   - `REACT_APP_API_URL`: Your Django backend URL
     - Local: `http://localhost:8000`
     - Production: `https://your-django-backend.onrender.com`

6. **Deploy!** ✅

### For Backend (Django on Render.com)

1. **Go to https://render.com**
2. **New Web Service**
3. **Settings:**
   - Build: `pip install -r requirements.txt`
   - Start: `gunicorn backend.wsgi`

### Result:
- **Frontend URL**: `https://your-app.vercel.app`
- **Backend URL**: `https://your-app.onrender.com`

Update Vercel environment variable with your Render backend URL once it's deployed!
