# LLM Multi-Agent Chat Platform

A full-stack, production-ready AI chatbot system using FastAPI, LangChain, LangGraph, and Streamlit.

---

## 🚀 Overview

This project is organized into **two separate branches** for maximum modularity and deployment flexibility:

- **backend:**  
  FastAPI-based API with endpoints for both LangChain and LangGraph LLM workflows.

- **frontend:**  
  Streamlit-based UI for interactive chat, with engine selection and conversation history.

---

## 🗂️ Branches

| Branch    | Purpose                                   | Main Technologies                |
|-----------|-------------------------------------------|----------------------------------|
| backend   | REST API with LangChain & LangGraph logic | FastAPI, LangChain, LangGraph    |
| frontend  | Chat UI with engine selection             | Streamlit, Python requests       |

Each branch has its own README.md with setup instructions.

---

## 🏗️ How to Use

1. **Clone the repo and switch to your desired branch:**

   ```bash
   # For backend (API)
   git clone <repo_url> -b backend backend
   cd backend
   # (See backend/README.md for full setup)

   # For frontend (UI)
   git clone <repo_url> -b frontend frontend
   cd frontend
   # (See frontend/README.md for full setup)
