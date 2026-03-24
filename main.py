import os
from dotenv import load_dotenv
from groq import Groq

# 1. INITIALIZATION: Load environment variables and set up the AI client
load_dotenv()
api_key = os.getenv("GROQ_API_KEY")
client = Groq(api_key=api_key)

# 2. INTERACTIVE LOOP: Keeps the program running so you can ask multiple questions
while True:
    # Get user input and remove extra spaces using .strip()
    user_topic = input("\nWhat GATE topic do you want to learn? (type 'quiz' or 'exit'): ").strip()

    # 3. EXIT CONDITION: Allows the user to close the program gracefully
    if user_topic.lower() == 'exit':
        print("Closing the GATE Professor. Good luck with your 6th Sem!")
        break
    
    # 4. PROMPT LOGIC: Decide whether to provide a quiz or an explanation
    if user_topic.lower() == 'quiz':
        # Instruction for a random GATE Multiple Choice Question
        prompt = "Provide one challenging MCQ for GATE CS with 4 options. Do not give the answer yet."
    else:
        # Instruction for a beginner-friendly topic summary
        prompt = f"Explain {user_topic} in 3 bullet points for a 6th semester engineering student."

    # 5. API CALL: Send the selected prompt to the Llama-3 model
    completion = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
    )

    # 6. OUTPUT: Print the AI's response to the terminal
    print("\n" + completion.choices[0].message.content)