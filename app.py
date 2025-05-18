import requests
import os

API_KEY = os.getenv("GEMINI_API_KEY")  # Or set directly
url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={API_KEY}"

headers = {
    "Content-Type": "application/json"
}

data = {
    "contents": [{
        "parts": [{"text": "it's a chat bot"}]
    }]
}

response = requests.post(url, headers=headers, json=data)
print(response.json())
