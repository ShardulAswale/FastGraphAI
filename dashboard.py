import streamlit as st
import importlib.util
from pathlib import Path
import inspect

st.set_page_config(page_title="🧠 Multi-Model LLM Chat", layout="centered")
st.title("🧠 Unified LLM Chat Interface")

models = {
    "Echo Bot": "Echo_Bot/chain.py",
    "Together AI": "Together_AI_Chatbot/chain.py",
    "Together AI + Streaming": "Together_AI_(Streaming)/chain.py",
    "LangGraph + TogetherAI": "LangChain_Chat/chain.py"
}

model_name = st.selectbox("Select a model:", list(models.keys()))
chain_path = models[model_name]

def load_chain(path: str):
    module_name = Path(path).stem
    spec = importlib.util.spec_from_file_location(module_name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod

mod = load_chain(chain_path)
run_chain = mod.run_chain

if "dashboard_chat" not in st.session_state:
    st.session_state.dashboard_chat = []

user_input = st.chat_input("Type a message...")

if user_input:
    st.session_state.dashboard_chat.append(("user", user_input))
    with st.spinner(f"Using {model_name}..."):
        stream_placeholder = st.empty()
        if len(inspect.signature(run_chain).parameters) == 2:
            reply = run_chain(user_input, stream_placeholder)
        else:
            reply = run_chain(user_input)
    st.session_state.dashboard_chat.append(("bot", reply))

for role, msg in st.session_state.dashboard_chat:
    with st.chat_message("user" if role == "user" else "assistant"):
        st.markdown(msg)
