"""
The main app
"""
import os
from flask import Flask, request, jsonify
import openai
from flask_cors import CORS
from dotenv import load_dotenv
from prompts import get_character_prompt


load_dotenv()

app = Flask(__name__)
CORS(app)
openai.api_key = os.environ.get('OPENAI_API_KEY')

@app.route('/')
def index():
    """
    Hello world test endpoint
    """
    return "hello world"

@app.route('/chat', methods=['GET', 'POST'])
def chat():
    """
    This function handles the /chat endpoint, which is called by the frontend to send a message to the AI.
    """
    print('/chat called')
    conversation = request.get_json().get('conversation', [])
    print(conversation)

    # If the conversation is more than 20 messages long, keep only the first and last 10
    if len(conversation) > 20:
        conversation = conversation[:10] + conversation[-10:]

    # Create a list of messages for the OpenAI API, mapping 'human' to 'user' and 'ai' to 'assistant'
    messages = [{"role": "user" if message['sender'] == "human" else "assistant", 
                 "content": message['text']} for message in conversation]
    
    return jsonify({"response": "hello world", })

if __name__ == '__main__':
    app.run(debug=True)
