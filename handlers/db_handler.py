from pymongo import MongoClient
from datetime import datetime

client = MongoClient("mongodb://localhost:27017")
db = client["janabhoomi"]
collection = db["entries"]

def save_entry(text, privacy):
    entry = {
        "text": text,
        "privacy": privacy,
        "timestamp": datetime.now().isoformat()
    }
    collection.insert_one(entry)

def get_entries(public_only=True):
    query = {"privacy": "పబ్లిక్"} if public_only else {}
    return list(collection.find(query).sort("timestamp", -1))