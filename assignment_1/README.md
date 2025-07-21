# 🛍️ Smart Store Agent

This project implements a simple conversational agent using Gemini 1.5 Pro that suggests products based on the user's needs.

## 💡 How it Works

- The user writes a natural sentence like:  
  `"I have a headache"`  
- The agent uses Gemini to understand the need and suggests a relevant product (e.g., a medicine).
- It also explains why that product is suggested.

## 🚀 Technologies Used

- 🧠 Gemini 1.5 flash (Google Generative AI)
- 💬 Chainlit for UI
- 🐍 Python
- 🔐 dotenv for secure API key loading
- ⚙️ uv for managing the virtual environment

## 🔧 How to Run

1. Install dependencies:
   ```bash
   uv pip install -r requirements.txt
