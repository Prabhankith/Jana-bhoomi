from pymongo import MongoClient, errors
from datetime import datetime
import os

# Prefer Streamlit secrets if available, else env vars, else localhost
try:
    import streamlit as st
    MONGO_URI = st.secrets.get("MONGO_URI", os.getenv("MONGO_URI", "mongodb://localhost:27017"))
    DB_NAME = st.secrets.get("DB_NAME", os.getenv("DB_NAME", "janabhoomi"))
except Exception:
    MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")
    DB_NAME = os.getenv("DB_NAME", "janabhoomi")

client = MongoClient(MONGO_URI, serverSelectionTimeoutMS=5000)
db = client[DB_NAME]
collection = db["entries"]

def save_entry(text, privacy):
    entry = {
        "text": text,
        "privacy": privacy,            # must match your UI ("పబ్లిక్" / "ప్రైవేట్")
        "timestamp": datetime.now().isoformat()
    }
    collection.insert_one(entry)

def get_entries(public_only=True):
    query = {"privacy": "పబ్లిక్"} if public_only else {}
    return list(collection.find(query).sort("timestamp", -1))
