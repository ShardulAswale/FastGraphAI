from langchain_openai import ChatOpenAI
import os
from dotenv import load_dotenv

load_dotenv()

llm = ChatOpenAI(
    api_key=os.getenv("TOGETHER_API_KEY"),
    base_url="https://api.together.xyz/v1",
    model="mistralai/Mistral-7B-Instruct-v0.1"
)

def run_chain(message: str) -> str:
    try:
        response = llm.invoke(message)
        return response.content
    except Exception as e:
        return f"❌ Error: {str(e)}"
