# country_info_toolkit.py

import os
import google.generativeai as genai

# Load Gemini API key
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Initialize the model
model = genai.GenerativeModel("gemini-1.5-flash")

# Static data for demonstration
def get_capital(country):
    capitals = {
        "pakistan": "Islamabad",
        "india": "New Delhi",
        "usa": "Washington, D.C.",
        "france": "Paris",
        "japan": "Tokyo"
    }
    return capitals.get(country.lower(), "Unknown")

def get_language(country):
    languages = {
        "pakistan": "Urdu",
        "india": "Hindi",
        "usa": "English",
        "france": "French",
        "japan": "Japanese"
    }
    return languages.get(country.lower(), "Unknown")

def get_population(country):
    populations = {
        "pakistan": "241 million",
        "india": "1.4 billion",
        "usa": "331 million",
        "france": "67 million",
        "japan": "125 million"
    }
    return populations.get(country.lower(), "Unknown")

# Final function to create the message
def get_country_info(country):
    capital = get_capital(country)
    language = get_language(country)
    population = get_population(country)

    prompt = f"""
Tell me about {country.title()}.
- Capital: {capital}
- Language: {language}
- Population: {population}

Now explain it in a friendly way.
    """

    response = model.generate_content(prompt)
    return response.text
