# AI Study Assistant (GATE Preparation)

This is a Python-based tool I built in my 6th semester to help with **GATE exam** preparation. It uses an AI model to explain complex engineering topics in simple, easy-to-remember points.

### Features:
* **Interactive Prompt:** Asks for a specific GATE topic (like OS or Distributed Systems).
* **AI Explanations:** Uses the **Llama 3.3 model** via Groq API for fast, 3-point summaries.
* **Environment Security:** Keeps API keys safe using a `.env` file and `.gitignore`.

### Tech Stack:
* **Python**
* **Groq Cloud API**
* **python-dotenv**
* **Git/GitHub**

### How to Run:
1. Clone the repo.
2. Create a `.env` file in the main folder.
3. Add your key: `GROQ_API_KEY=your_actual_key_here`.
4. Run `python main.py`.

---
*Current Status: 6th Semester Project - Version 1.0*