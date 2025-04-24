from fastapi import FastAPI
from pydantic import BaseModel
from chain import run_langchain
from graph import run_langgraph

app = FastAPI(
    title="LLM Multi-Agent API",
    description="Chatbot API with LangChain and LangGraph endpoints.",
    version="1.0.0"
)

class ChatRequest(BaseModel):
    message: str

class ChatResponse(BaseModel):
    response: str

@app.post("/chat/chain", response_model=ChatResponse)
async def chat_chain(req: ChatRequest):
    reply = run_langchain(req.message)
    return {"response": reply}

@app.post("/chat/graph", response_model=ChatResponse)
async def chat_graph(req: ChatRequest):
    reply = run_langgraph(req.message)
    return {"response": reply}
