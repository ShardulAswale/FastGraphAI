# FastGraphAI Backend

FastAPI service for comparing LangChain LLM calls and LangGraph workflows.

## API

| Route | Method | Purpose |
| --- | --- | --- |
| /chat/chain | POST | Invoke the LangChain model wrapper |
| /chat/graph | POST | Run the LangGraph LLM workflow |
| /docs | GET | Interactive OpenAPI documentation |

Both chat routes accept `{"message": "Hello"}` and return `{"response": "..."}`. Pydantic defines the request and response schemas.

## Run locally

```bash
git clone --branch ChatBot_V3_Backend https://github.com/ShardulAswale/FastGraphAI.git fastgraphai-backend
cd fastgraphai-backend
python -m venv .venv
# Linux/macOS: source .venv/bin/activate
# Windows PowerShell: .venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

Create a local `.env` file with `TOGETHER_API_KEY=<your-key>` or set the environment variable, then start:

```bash
python -m uvicorn app:app --reload --port 8000
```

The checked-in model wrapper uses Together.ai's OpenAI-compatible API. Provider calls require credentials and may incur charges.

## Structure

- `app.py` — routes and typed API schemas.
- `chain.py` — model configuration and LangChain invocation.
- `graph.py` — state schema and a single-node LangGraph workflow.
- `requirements.txt` — Python dependencies.

## Scope

This branch demonstrates LLM integration and API structure. The current workflow contains one LLM node. Authentication, rate limiting and automated evaluation can be added as further development.

[Project overview and frontend instructions](https://github.com/ShardulAswale/FastGraphAI)
