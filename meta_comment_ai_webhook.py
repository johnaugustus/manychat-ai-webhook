from flask import Flask, request, jsonify
from openai import openAI
import os

app = Flask(__name__)
CLIENT = OpenAI ()

@app.route("/")
def home():
    return "Bot is live"
    
    @app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    user_message = data.get("message", "")
    
    prompt = f"""
You are a smart assistant focused on:
- African development
- Adoption of innovations
- Practical education

Reply in a simple, engaging, and helpful way.

User message: {user_message}
"""

    response = client.chat.completion.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]
    )

    ai_reply = response.choices[0].message.content

    return jsonify({
        "ai_reply": ai_reply
    })

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
