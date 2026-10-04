# FastGraphAI

A Python LLM chat project comparing **LangChain** model calls with **LangGraph** workflow orchestration, exposed through **FastAPI** and a **Streamlit** interface.

## What it demonstrates

- Typed request and response schemas with Pydantic.
- Separate API routes for LangChain and LangGraph.
- OpenAI-compatible model integration using Together.ai in the checked-in backend.
- A Streamlit interface with engine selection and session conversation history.
- Separation of API and interface code across branches.

The current graph is a single LLM node. This repository is a learning and portfolio project; the checked-in implementation does not establish a production-ready multi-agent system.

## Find the implementation

| Branch | Contents |
| --- | --- |
| [ChatBot_V3_Backend](https://github.com/ShardulAswale/FastGraphAI/tree/ChatBot_V3_Backend) | FastAPI service, LangChain call, LangGraph workflow and dependency list |
| [ChatBot_V3_Frontend](https://github.com/ShardulAswale/FastGraphAI/tree/ChatBot_V3_Frontend) | Streamlit chat interface |
| [main](https://github.com/ShardulAswale/FastGraphAI/tree/main) | Initial API implementation and this overview |
| [LangGraph-Workflow](https://github.com/ShardulAswale/FastGraphAI/tree/LangGraph-Workflow) | Separate workflow experiments |

## Run the backend

```bash
git clone --branch ChatBot_V3_Backend https://github.com/ShardulAswale/FastGraphAI.git fastgraphai-backend
cd fastgraphai-backend
python -m venv .venv
# Linux/macOS: source .venv/bin/activate
# Windows PowerShell: .venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

Set `TOGETHER_API_KEY` in your local environment or a local `.env` file, then run:

```bash
python -m uvicorn app:app --reload --port 8000
```

Explore the API at `http://localhost:8000/docs`.

| Route | Method | Request |
| --- | --- | --- |
| /chat/chain | POST | `{"message": "Explain retrieval-augmented generation"}` |
| /chat/graph | POST | Same schema |

Both routes return `{"response": "..."}`.

## Run the interface

In a separate folder and terminal:

```bash
git clone --branch ChatBot_V3_Frontend https://github.com/ShardulAswale/FastGraphAI.git fastgraphai-frontend
cd fastgraphai-frontend
python -m venv .venv
# Activate the virtual environment as above.
python -m pip install -r requirements.txt requests
```

Set `BACKEND_URL=http://localhost:8000` in a local `.env` file, then run:

```bash
python -m streamlit run app.py
```

The frontend makes Python HTTP requests to the backend. Its default URL should be overridden for your own environment.

## Project scope

This implementation demonstrates LLM API integration and workflow structure. Authentication, rate limiting, persistent chat history, automated evaluation and comprehensive deployment hardening are future work. Model calls may incur provider charges. Keep real API keys out of commits.
