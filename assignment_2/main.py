# main.py
import chainlit as cl
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load Gemini API key
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Use Gemini 1.5 Flash if needed
MODEL = genai.GenerativeModel("gemini-1.5-flash")

def detect_mood(user_input):
    prompt = f"What is the user's mood in this sentence: '{user_input}'? Just return a one-word mood like happy, sad, stressed, etc."
    response = MODEL.generate_content(prompt)
    return response.text.strip().lower()

def suggest_activity(mood):
    prompt = f"The user is feeling {mood}. Suggest a helpful activity with a short reason."
    response = MODEL.generate_content(prompt)
    return response.text.strip()

@cl.on_message
async def handle_message(message: cl.Message):
    user_input = message.content
    mood = detect_mood(user_input)

    if mood in ["sad", "stressed"]:
        activity = suggest_activity(mood)
        result = f"🧠 Mood Detected: **{mood}**\n💡 Activity: {activity}"
    else:
        result = f"🙂 Mood Detected: **{mood}**. No handoff needed."

    await cl.Message(content=result).send()
