from flask import Flask, request, jsonify
from google import genai
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-2.0-pro")

app = Flask(__name__)

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message")
    response = model.generate_content(user_input)
    return jsonify({"response": response.text})

if __name__ == "__main__":
    app.run(debug=True)
