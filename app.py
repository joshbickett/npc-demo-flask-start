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

if __name__ == '__main__':
    app.run(debug=True)
