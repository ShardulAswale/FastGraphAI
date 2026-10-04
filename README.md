# FastGraphAI Frontend

Streamlit chat interface for the FastGraphAI backend, with LangChain/LangGraph engine selection and conversation history held in Streamlit session state.

## Run locally

```bash
git clone --branch ChatBot_V3_Frontend https://github.com/ShardulAswale/FastGraphAI.git fastgraphai-frontend
cd fastgraphai-frontend
python -m venv .venv
# Linux/macOS: source .venv/bin/activate
# Windows PowerShell: .venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt requests
```

Start the [backend](https://github.com/ShardulAswale/FastGraphAI/tree/ChatBot_V3_Backend) separately. Create a local `.env` containing:

```dotenv
BACKEND_URL=http://localhost:8000
```

Then run:

```bash
python -m streamlit run app.py
```

The interface sends Python HTTP requests to `/chat/chain` or `/chat/graph`. Override `BACKEND_URL` for your own API rather than relying on the default deployment URL.

## What it demonstrates

- Streamlit chat input and message rendering.
- Selection between two LLM workflow endpoints.
- HTTP API integration and response handling.
- Session-based UI state.

[Project overview](https://github.com/ShardulAswale/FastGraphAI)
