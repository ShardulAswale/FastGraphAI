from fastapi import FastAPI, Request
from graph import run_graph

app = FastAPI(title="LangGraph API")

@app.get("/")
def read_root():
    return {"message": "Hello from FastAPI + LangGraph"}

@app.post("/chat")
async def chat(request: Request):
    body = await request.json()
    user_input = body.get("message", "")
    response = run_graph(user_input)
    return {"response": response}
