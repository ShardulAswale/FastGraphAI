import streamlit as st
from chain import run_chain

st.set_page_config(page_title="LangChain Echo Bot", layout="centered")
st.title("💬 LangChain Chat (No OpenAI)")

# Session state for chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Input from user
user_input = st.chat_input("Type a message...")

# Handle message
if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.spinner("Thinking..."):
        response = run_chain(user_input)
    st.session_state.messages.append({"role": "assistant", "content": response})

# Display chat
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])
