import streamlit as st
from chain import run_chain

st.set_page_config(page_title="LangChain Chatbot", layout="centered")
st.title("LangChain + Together.ai Chat")

if "messages" not in st.session_state:
    st.session_state.messages = []

user_input = st.chat_input("Say something...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.spinner("Thinking..."):
        response = run_chain(user_input)
    st.session_state.messages.append({"role": "assistant", "content": response})

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])
