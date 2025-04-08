import streamlit as st
import importlib.util
from pathlib import Path

st.set_page_config(page_title="🧠 Multi-Model LLM Chat", layout="centered")
st.title("🧠 Unified LLM Chat Interface")

# 📁 Available models and their chain.py paths
models = {
    "Echo Bot": "langchain+streamlit/chain.py",
    "Together AI": "langchain+togetherai/chain.py"
}

# 🔽 Model selector
model_name = st.selectbox("Select a model:", list(models.keys()))
chain_path = models[model_name]

# 📦 Dynamically load run_chain from the selected model's chain.py
def load_run_chain(path: str):
    module_name = Path(path).stem
    spec = importlib.util.spec_from_file_location(module_name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.run_chain

run_chain = load_run_chain(chain_path)

# 💬 Chat logic
if "dashboard_chat" not in st.session_state:
    st.session_state.dashboard_chat = []

user_input = st.chat_input("Type a message...")

if user_input:
    st.session_state.dashboard_chat.append(("user", user_input))
    with st.spinner(f"Using {model_name}..."):
        reply = run_chain(user_input)
    st.session_state.dashboard_chat.append(("bot", reply))

# 💬 Display chat history
for role, msg in st.session_state.dashboard_chat:
    with st.chat_message("user" if role == "user" else "assistant"):
        st.markdown(msg)
