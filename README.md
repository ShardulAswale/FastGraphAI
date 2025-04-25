# LLM Chat Backend (FastAPI, LangChain & LangGraph)

This is the **backend** for the LLM Multi-Agent Chat platform.  
It provides REST API endpoints for LLM-powered chat using both LangChain and LangGraph logic, designed for production, cloud deployment (Render, Railway, etc.), and local development.

---

## 🚀 Features

- `/chat/chain` — LangChain agent endpoint (OpenAI-compatible LLMs)  
- `/chat/graph` — LangGraph workflow endpoint (graph-based LLM logic)  
- **OpenAPI/Swagger UI** at `/docs`  
- **CORS enabled** (for safe frontend/remote access)  
- Uses Together.ai (or any OpenAI-compatible endpoint)  

---

## 🗂️ Structure

```
backend/
├── app.py         # FastAPI application and endpoints
├── chain.py       # LangChain agent logic
├── graph.py       # LangGraph workflow logic
├── requirements.txt
├── .env.example   # Example for secrets/config
└── README.md
```

---

## 🛠️ Setup & Installation

### 1. Clone the backend branch

```bash
git clone <repo_url> -b backend backend
cd backend
```

### 2. Install requirements

```bash
pip install -r requirements.txt
```

### 3. Set up environment variables

Copy `.env.example` to `.env` and fill in your Together.ai or OpenAI API key.

```
TOGETHER_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxx
```

### 4. Run the server (locally)

```bash
uvicorn app:app --host 0.0.0.0 --port 8000 
or 
python -m uvicorn app:app --host 0.0.0.0 --port 8000
```

- The API will be live at [http://localhost:8000](http://localhost:8000)  
- The API docs are at [http://localhost:8000/docs](http://localhost:8000/docs)  

---

## ⚙️ Endpoints

| Route           | Method | Description                |
|-----------------|--------|----------------------------|
| `/chat/chain`   | POST   | LangChain LLM chat         |
| `/chat/graph`   | POST   | LangGraph workflow chat    |
| `/docs`         | GET    | OpenAPI/Swagger UI         |

#### Request (POST body)
```json
{
  "message": "Hello world"
}
```

#### Response
```json
{
  "response": "LLM reply here"
}
```

---

## ⚙️ Environment Variables

| Name             | Description                     |
|------------------|---------------------------------|
| TOGETHER_API_KEY | Together.ai API key (required)  |

---

## 🟢 Deployment

- Deployable to **Render, Railway, Hugging Face Spaces**, etc.
- Set your API key(s) as environment variables in the dashboard.
- Use `uvicorn app:app --host 0.0.0.0 --port 8000` as the start command.

---

## 🛡️ Security

- **Never commit your real `.env`!** Always add `.env` to `.gitignore`.
- Only share `.env.example` for safe config sharing.

---

## 🤝 Contributing

Pull requests and issues are welcome!  
Please open an issue for questions or feature requests.

---

## 📞 Contact

For help or inquiries, open a GitHub issue or contact the maintainer.
