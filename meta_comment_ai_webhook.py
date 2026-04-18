from flask import Flask, request, jsonify
from openai import OpenAI
import os

app = Flask(__name__)

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))


@app.route("/")
def home():
    return "Bot is live", 200


@app.route("/webhook", methods=["POST"])
def webhook():
    try:
        data = request.get_json(silent=True) or {}
        user_message = data.get("message", "").strip()

        if not user_message:
            return jsonify({"reply": "No message received."}), 400

        prompt = f"""
You are a smart assistant focused on:
- African development
- Adoption of innovations
- Practical education

Reply in a simple, engaging, and helpful way.

User message: {user_message}
"""

        response = client.responses.create(
            model="gpt-4o-mini",
            input=prompt
        )

        reply_text = response.output_text.strip()

        return jsonify({"reply": reply_text}), 200

    except Exception as e:
        return jsonify({"reply": f"Error: {str(e)}"}), 500


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
