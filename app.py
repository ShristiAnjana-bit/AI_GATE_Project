# ==========================================
# ZONE 1: THE FOUNDATION
# ==========================================
import streamlit as st
import os
from dotenv import load_dotenv
from groq import Groq
from fpdf import FPDF

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

st.set_page_config(page_title="GATE AI Professor Pro", layout="wide")

# Custom CSS for clean UI
st.markdown("""
    <style>
    .stWrite { line-height: 1.6; font-size: 1.1rem; }
    .stButton>button { background-color: #007bff; color: white; border-radius: 8px; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

# ==========================================
# ZONE 2: FUNCTIONS & STATE
# ==========================================
def create_pdf(text):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    clean_text = text.encode('latin-1', 'ignore').decode('latin-1')
    pdf.multi_cell(0, 10, txt=clean_text)
    return pdf.output(dest="S").encode("latin-1")

if "messages" not in st.session_state: st.session_state.messages = []
if "current_quiz" not in st.session_state: st.session_state.current_quiz = None
if "score" not in st.session_state: st.session_state.score = 0

# ==========================================
# ZONE 3: SIDEBAR
# ==========================================
with st.sidebar:
    st.title("🎯 FAANG Goal")
    st.metric(label="Student Score", value=f"{st.session_state.score} pts")
    st.progress(95) # LOGIC IS COMPLETE!
    st.divider()
    mode = st.radio("Mode:", ["👨‍🏫 Tutor Chat", "📝 Smart Quiz"])
    if st.button("🗑️ Reset Everything"):
        st.session_state.clear()
        st.rerun()

# ==========================================
# ZONE 4: TUTOR CHAT
# ==========================================
if mode == "👨‍🏫 Tutor Chat":
    st.title("🎓 AI GATE Professor")
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]): st.markdown(msg["content"])

    user_query = st.chat_input("Ask a GATE concept...")
    if user_query:
        st.session_state.messages.append({"role": "user", "content": user_query})
        with st.chat_message("user"): st.markdown(user_query)
        
        with st.chat_message("assistant"):
            res = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=st.session_state.messages
            ).choices[0].message.content
            st.markdown(res)
            st.session_state.messages.append({"role": "assistant", "content": res})
            st.download_button("📄 Download Note", create_pdf(res), "gate_notes.pdf")

# ==========================================
# ZONE 5: SMART QUIZ (The Formatting Fix)
# ==========================================
elif mode == "📝 Smart Quiz":
    st.title("📝 Smart GATE Evaluator")
    topic = st.text_input("Enter Subject (e.g., BST, OS, DBMS):")

    if st.button("Generate Quiz"):
        with st.spinner("Preparing exam..."):
            # STRICTOR PROMPT to fix the layout in your screenshot
            prompt = (
                f"Generate 3 difficult GATE MCQs on {topic}. "
                "CRITICAL FORMATTING: Each option MUST be on one line like 'A. Option Text'. "
                "Do not put a newline between the letter and the text. Do not show answers."
            )
            st.session_state.current_quiz = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[{"role": "user", "content": prompt}]
            ).choices[0].message.content

    if st.session_state.current_quiz:
        st.markdown("### Your Exam Paper")
        st.divider()
        
        # LOOP FIX: This ensures each line is treated as a separate block
        lines = st.session_state.current_quiz.split('\n')
        for line in lines:
            if line.strip():
                st.write(line)
        
        st.divider()
        user_ans = st.text_input("Submit Answers (e.g., 1A, 2B, 3C):")
        
        if st.button("Grade Me"):
            with st.spinner("Checking..."):
                grade_p = f"Quiz: {st.session_state.current_quiz}\nUser: {user_ans}\nGrade out of 30."
                feedback = client.chat.completions.create(
                    model="llama-3.3-70b-versatile",
                    messages=[{"role": "user", "content": grade_p}]
                ).choices[0].message.content
                st.info(feedback)
                
                if "30/30" in feedback or "3/3" in feedback:
                    st.session_state.score += 30
                    st.balloons()

