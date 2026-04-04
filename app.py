import streamlit as st
import os
from dotenv import load_dotenv
from groq import Groq

# 1. INITIALIZATION
load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

st.set_page_config(page_title="GATE AI Professor", page_icon="🎓")

# Initialize chat history if it doesn't exist
if "messages" not in st.session_state:
    st.session_state.messages = []

# 2. SIDEBAR
with st.sidebar:
    st.title("🎯 My FAANG Goal")
    st.write("6th Semester Progress")
    st.progress(25)
    st.info("Focus: AI Projects & GATE Prep")

# 3. MAIN INTERFACE
st.title("🎓 AI GATE Professor")

# Display previous chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 4. CHAT LOGIC
user_query = st.chat_input("Ask a GATE question or type 'quiz'...")

if user_query:
    # Display user message
    with st.chat_message("user"):
        st.markdown(user_query)
    st.session_state.messages.append({"role": "user", "content": user_query})

    # Generate AI response
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            try:
                response = client.chat.completions.create(
                    model="llama-3.3-70b-versatile",
                    messages=st.session_state.messages # Sends whole history!
                )
                response_text = response.choices[0].message.content
                st.markdown(response_text)
                st.session_state.messages.append({"role": "assistant", "content": response_text})
            except Exception as e:
                st.error(f"⚠️ Connection Error: {e}")