import streamlit as st
import requests
import os
from dotenv import load_dotenv

load_dotenv()
BACKEND_URL = os.getenv("BACKEND_URL", "https://fastgraphai-frontend.onrender.com")

st.set_page_config(page_title="LLM Chat Frontend", layout="centered")
st.title("💬 LLM Chat (Streamlit Frontend)")

if "messages" not in st.session_state:
    st.session_state.messages = []

# Dropdown for endpoint selection (LangChain or LangGraph)
endpoint = st.selectbox(
    "Choose LLM engine:",
    [("/chat/chain", "LangChain"), ("/chat/graph", "LangGraph")],
    format_func=lambda x: x[1]
)

user_input = st.chat_input("Type a message...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.spinner("Talking to backend..."):
        try:
            resp = requests.post(
                f"{BACKEND_URL}{endpoint[0]}",
                json={"message": user_input},
                timeout=60
            )
            reply = resp.json().get("response", "❌ API error")
        except Exception as e:
            reply = f"❌ Backend error: {e}"
    st.session_state.messages.append({"role": "assistant", "content": reply})

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])
