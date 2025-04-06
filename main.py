from fastapi import FastAPI
from pydantic import BaseModel
from graph import run_graph

app = FastAPI(title="LangGraph API")

class ChatRequest(BaseModel):
    message: str

@app.get("/")
def read_root():
    return {"message": "Hello from FastAPI + LangGraph"}

@app.post("/chat")
async def chat(request: ChatRequest):
    response = run_graph(request.message)
    return {"response": response}
