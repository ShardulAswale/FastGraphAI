import subprocess
import time

services = {
    "Dashboard (8501)": [
        "streamlit", "run", "dashboard.py", "--server.port=8501"
    ],
    "Together AI (8502)": [
        "streamlit", "run", "Together_AI_Chatbot/main.py", "--server.port=8502"
    ],
    "Together AI + Streaming (8503)": [
        "streamlit", "run", "Together_AI_(Streaming)/main.py", "--server.port=8503"
    ],
    "LangGraph + TogetherAI (8504)": [
        "streamlit", "run", "LangChain_Chat/main.py", "--server.port=8504"
    ],
    "Echo Bot (8505)": [
        "streamlit", "run", "Echo_Bot/main.py", "--server.port=8505"
    ]
}

print("🚀 Starting all services...")

for name, cmd in services.items():
    print(f"🔹 {name}")
    subprocess.Popen(cmd)
    time.sleep(1)

print("\n✅ All services are running!")
print("Open your dashboard at http://localhost:8501")
