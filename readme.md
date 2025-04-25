# streamlit_langchain_api

A simple LangChain-style FastAPI backend with a `/chat` endpoint. Accepts a message and returns an echo response.

## 🚀 Run the API

```bash
pip install -r requirements.txt
uvicorn main:app --reload --port 8502
