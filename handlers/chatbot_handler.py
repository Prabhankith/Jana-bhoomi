import os
import requests

# Try importing Streamlit secrets (works only when running inside Streamlit Cloud)
try:
    import streamlit as st
    STREAMLIT_AVAILABLE = True
except ImportError:
    STREAMLIT_AVAILABLE = False

# ✅ Get API Key: first check Streamlit secrets, then fallback to .env
def get_dify_api_key():
    key = None
    if STREAMLIT_AVAILABLE:
        try:
            key = st.secrets["DIFY_API_KEY"]
        except Exception:
            pass
    return key or os.getenv("DIFY_API_KEY")


DIFY_API_KEY = get_dify_api_key()
BASE_URL = "https://api.dify.ai/v1"  # Dify endpoint (don’t change)

def ask_dify(message: str) -> str:
    """
    Sends a message to the Dify chatbot and returns the response text.
    """
    if not DIFY_API_KEY:
        return "⚠️ Missing DIFY_API_KEY. Please configure it in .env or Streamlit Secrets."

    headers = {
        "Authorization": f"Bearer {DIFY_API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
    "inputs": {},
    "query": message,
    "response_mode": "blocking",
    "user": "janabhoomi-user"   # can be any string, ideally unique per user
    }


    try:
        response = requests.post(f"{BASE_URL}/chat-messages", json=payload, headers=headers)
        response.raise_for_status()
        data = response.json()
        return data.get("answer", "⚠️ No response from chatbot.")
    except Exception as e:
        return f"⚠️ Chatbot error: {e}"
