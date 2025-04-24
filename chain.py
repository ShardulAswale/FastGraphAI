import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()
TOGETHER_API_KEY = os.getenv("TOGETHER_API_KEY")

llm = ChatOpenAI(
    api_key=TOGETHER_API_KEY,
    base_url="https://api.together.xyz/v1",
    model="mistralai/Mistral-7B-Instruct-v0.1"
)

def run_langchain(message: str) -> str:
    try:
        response = llm.invoke(message)
        return response.content
    except Exception as e:
        return f"[LangChain Error] {e}"
