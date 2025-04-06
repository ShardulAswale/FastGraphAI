from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
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

@app.get("/ui", response_class=HTMLResponse)
def chat_ui():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>LangServe Chat</title>
        <style>
            body { font-family: Arial, sans-serif; padding: 2rem; }
            input, button { font-size: 1rem; padding: 0.5rem; }
            #response { margin-top: 1rem; }
        </style>
    </head>
    <body>
        <h2>LangServe Chat</h2>
        <input type="text" id="message" placeholder="Ask me something..." size="40" />
        <button onclick="sendMessage()">Send</button>
        <div id="response"></div>

        <script>
            async function sendMessage() {
                const message = document.getElementById('message').value;
                const res = await fetch('/chat', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ message })
                });
                const data = await res.json();
                document.getElementById('response').innerText = data.response;
            }
        </script>
    </body>
    </html>
    """
