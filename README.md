# 🎓 AI GATE Study Assistant

An interactive, AI-powered CLI tool designed for **6th-semester engineering students** to master Computer Science concepts and prepare for the **GATE Exam**.

## 🚀 Key Features
- **Strict Professor Mode:** Get technical, 3-point summaries of complex CS topics (Operating Systems, DBMS, Computer Networks).
- **Interactive Quiz Engine:** Generates challenging MCQs focused on the GATE syllabus.
- **Real-time Feedback:** The AI listens to your answer, corrects mistakes, and explains the underlying logic so you learn from every error.
- **Secure Architecture:** Implements `.env` masking to protect API credentials, following industry-standard security practices.

## 🛠️ Tech Stack
- **Language:** Python 3.x
- **Model:** Llama-3.3-70b (via Groq Cloud)
- **API:** Groq SDK
- **Security:** `python-dotenv` for API key protection
- **Version Control:** Git & GitHub

## 📂 Project Structure
- `main.py`: The core interactive engine and multi-step conversation logic.
- `.env`: (Private) Stores the secret `GROQ_API_KEY`.
- `.gitignore`: Ensures sensitive configuration data is never leaked.

## 📖 How to Run
1. Clone the repository.
2. Create a `.env` file in the root directory.
3. Add your key: `GROQ_API_KEY=your_key_here`.
4. Run the script:
   ```bash
   python main.py