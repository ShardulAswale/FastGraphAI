from fastapi import FastAPI, Request, Query
from fastapi.responses import HTMLResponse,JSONResponse, PlainTextResponse
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

from fastapi import Request, Query
from fastapi.responses import JSONResponse, PlainTextResponse

@app.get(
    "/chat",
    response_class=PlainTextResponse,
    responses={
        200: {
            "content": {
                "text/plain": {
                    "example": "It's 24°C and sunny ☀️"
                },
                "application/json": {
                    "example": {
                        "response": "It's 24°C and sunny ☀️"
                    }
                }
            },
            "description": "Returns a response as plain text or JSON based on Accept header",
        }
    }
)
def chat_get(
    request: Request,
    message: str = Query(..., description="Your input message")
):
    response = run_graph(message)

    accept = request.headers.get("accept", "")
    if "application/json" in accept:
        return JSONResponse(content={"response": response})
    else:
        return PlainTextResponse(content=response)



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
