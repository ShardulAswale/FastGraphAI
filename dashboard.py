import streamlit as st
import json
import requests
from service_call import call_service

# Load available services
with open('services.json', 'r') as f:
    services = json.load(f)

st.set_page_config(page_title="AI Service Dashboard", layout="centered")
st.title("🧠 AI Microservices Dashboard")

service_name = st.selectbox("Choose a service:", list(services.keys()))
endpoint = services[service_name]

user_input = st.text_input("Enter your message:", placeholder="Ask something...")

if st.button("Send") and user_input:
    with st.spinner("Thinking..."):
        response = call_service(endpoint, user_input)
    st.markdown("### Response:")
    st.code(response, language='markdown')
