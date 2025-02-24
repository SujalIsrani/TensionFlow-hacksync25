from flask import Flask, render_template, request, jsonify
import google.generativeai as genai
import os
from dotenv import load_dotenv
import pyttsx3  # Text-to-Speech for "Listen to Story"

app = Flask(__name__)
STARRYAI_API_KEY = "RoqgI2YZcaJzv0qhvoUyympLtPZXPg"

# Load API key from .env
load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=API_KEY)
model = genai.GenerativeModel("gemini-1.5-flash")

# Function to generate a short story segment
def generate_story(prompt, genre, style, intent, length, language):
    system_prompt = (
        f"Write a {genre.lower()} story in {style.lower()} style and {language.lower()} for {intent.lower()} purposes. "
        "Keep it immersive but generate only a small paragraph."
    )
    max_tokens = {"Short": 100, "Medium": 200, "Long": 300}.get(length, 100)
    response = model.generate_content(
        [system_prompt, prompt], generation_config={"max_output_tokens": max_tokens}
    )
    return response.text if response and response.text else "Oops! Something went wrong."

# Function to continue the story
def continue_story(existing_story, length):
    system_prompt = "Continue the following story while maintaining its style and tone."
    max_tokens = {"Short": 100, "Medium": 200, "Long": 300}.get(length, 100)
    response = model.generate_content(
        [system_prompt, existing_story], generation_config={"max_output_tokens": max_tokens}
    )
    return response.text.strip() if response and response.text else "Could not continue the story."

# Function to suggest a title
def suggest_title(story):
    system_prompt = "Generate a creative and engaging title for the following story."
    response = model.generate_content([system_prompt, story])
    return response.text.strip() if response and response.text else "No title generated."

# Function to conclude the story
def conclude_story(story):
    system_prompt = "Write a satisfying conclusion to this story."
    response = model.generate_content([system_prompt, story])
    return response.text.strip() if response and response.text else "No conclusion generated."

# Function to convert text to speech
def text_to_speech(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
    return "Audio played successfully."

@app.route('/')
def landing():
    return render_template('landing.html')

@app.route('/main')
def main():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    data = request.json
    prompt = data.get("prompt", "")
    genre = data.get("genre", "Fantasy")
    style = data.get("style", "Descriptive")
    intent = data.get("intent", "Idea Generation")
    length = data.get("length", "Short")
    language = data.get("language","English") 

    story = generate_story(prompt, genre, style, intent, length, language)
    return jsonify({"story": story})

@app.route('/continue_story', methods=['POST'])
def continue_story_route():
    data = request.json
    story = data.get("story", "")
    length = data.get("length", "Short")
    new_story_part = continue_story(story, length)
    return jsonify({"new_story": new_story_part})

@app.route('/suggest_title', methods=['POST'])
def suggest_title_route():
    data = request.json
    story = data.get("story", "")
    title = suggest_title(story)
    return jsonify({"title": title})

@app.route('/conclude_story', methods=['POST'])
def conclude_story_route():
    data = request.json
    story = data.get("story", "")
    conclusion = conclude_story(story)
    return jsonify({"conclusion": conclusion})

@app.route('/listen', methods=['POST'])
def listen():
    data = request.json
    story = data.get("story", "")
    text_to_speech(story)
    return jsonify({"message": "Listening to story..."})

@app.route('/generate_image', methods=['POST'])
def generate_image():
    data = request.json
    story_text = data.get("story", "")

    if not story_text:
        return jsonify({"error": "Story text is required for image generation"}), 400

    headers = {"Authorization": f"Bearer {STARRYAI_API_KEY}"}
    payload = {"prompt": story_text, "style": "artistic", "resolution": "hd"}

    response = request.post("https://api.starryai.com/generate", json=payload, headers=headers)

    if response.status_code == 200:
        image_url = response.json().get("image_url")
        return jsonify({"image_url": image_url})
    else:
        return jsonify({"error": "Failed to generate image", "details": response.text}), 500

if __name__ == '__main__':
    app.run(debug=True)
