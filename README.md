# LangServe

A minimal project using FastAPI and LangGraph with auto-deploy via GitHub Actions.

## 🚀 Run Locally
```bash
pip install -r requirements.txt
uvicorn main:app --reload
```

Visit `http://127.0.0.1:8000/docs`

## 🌍 Deploy on Render
1. Push this project to GitHub
2. Go to [Render.com](https://render.com/)
3. New → Web Service → Connect repo
4. Set:
   - Build: `pip install -r requirements.txt`
   - Start: `uvicorn main:app --host 0.0.0.0 --port 10000`

## 🔁 GitHub Actions Deployment
- Get your **Deploy Hook** URL from Render
- Add it as a GitHub secret: `RENDER_DEPLOY_HOOK`
- Push to `main` and it auto-deploys!
