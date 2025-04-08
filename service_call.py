import requests

def call_service(endpoint: str, message: str) -> str:
    try:
        response = requests.post(endpoint, json={"message": message})
        if response.ok:
            return response.json().get("response", "No response key in JSON.")
        else:
            return f"❌ Error {response.status_code}: {response.text}"
    except Exception as e:
        return f"⚠️ Exception occurred: {str(e)}"
