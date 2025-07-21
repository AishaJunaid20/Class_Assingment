# 😊 Mood Analyzer with Handoff

This app uses two AI agents to analyze the user's mood and suggest an activity if the mood is negative.

## 🔄 Process

1. **Agent 1**: Detects the user's mood (e.g., "happy", "sad", "stressed") based on their message.
2. **Agent 2**: If the mood is "sad" or "stressed", it suggests an uplifting activity like:
   > "Take a short walk to refresh your mind."

## 👩‍💻 Technologies Used

- 🧠 Gemini 1.5 Pro (Google Generative AI)
- ⚡ Chainlit (real-time interaction)
- 🐍 Python
- 📦 uv for package management
- 🔐 dotenv for secret API key handling

## 🏃‍♀️ How to Run

1. Install dependencies:
   ```bash
   uv pip install -r requirements.txt
   ```

2. Add your Gemini API key in `.env`:
   ```
   GOOGLE_API_KEY=your_api_key_here
   ```

3. Run the app:
   ```bash
   chainlit run main.py
   ```

## 📋 Example

User:  
```
Exams are killing me
```

Output:  
- Detected Mood: **stressed**
- Suggested Activity: *"Try a short meditation session to calm your mind."*
