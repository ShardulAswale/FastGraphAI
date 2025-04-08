import subprocess
import time

services = {
    "LangChain Echo Bot": ["streamlit", "run", "langchain+streamlit/main.py", "--server.port=8501"],
    "LangChain + Together.ai": ["streamlit", "run", "langchain+openai/main.py", "--server.port=8502"],
    "LLM Dashboard": ["streamlit", "run", "dashboard.py", "--server.port=8503"]
}

print("🚀 Launching free LLM services...")

for name, cmd in services.items():
    print(f"🔹 Starting {name}")
    subprocess.Popen(cmd)
    time.sleep(1)

print("✅ All services launched. Visit http://localhost:8503")
