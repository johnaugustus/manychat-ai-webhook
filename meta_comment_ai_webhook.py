from flask import Flask, request, jsonify
import openai
import os

app = Flask(__name__)

openai.api_key = os.getenv("OPENAI_API_KEY")

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

    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]
    )

    ai_reply = response['choices'][0]['message']['content']

    return jsonify({
        "ai_reply": ai_reply
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
