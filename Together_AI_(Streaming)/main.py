import streamlit as st
from chain import run_chain

st.set_page_config(page_title="Together AI (Streaming)", layout="centered")
st.title("🔄 Together AI Chatbot (Streaming Output)")

if "messages" not in st.session_state:
    st.session_state.messages = []

user_input = st.chat_input("Ask me something...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.spinner("Streaming response..."):
        st_callback = st.empty()
        streamed_response = run_chain(user_input, st_callback)
    st.session_state.messages.append({"role": "assistant", "content": streamed_response})  # ONLY ONCE!

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])
