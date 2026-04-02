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
        completions = client.chat.completions.create(
            model = "llama-3.3-70b-versatile",
            messages=[{"role":"user","content":prompt}]
        )
        question_text = completions.choices[0].message.content
        print("\n"+question_text)

        #step B: Pause and wait for you to type the answer
        user_answer = input("\n Your Answer(A/B/C/D):").strip().upper()

        #step c: Send your answer back to the Professor for checking
        feedback_prompt =f"The question was:{question_text}.The student answered:{user_answer}. Is it correct? If wrong,tell the correct option and explain."
        feedback_result = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role":"user","content":feedback_prompt}],
        )
        #this prints the final verdict
        print("\n---PROFESSOR'S FEEDBACK---")
        print(feedback_result.choices[0].message.content)
    else:
        # Instruction for a beginner-friendly topic summary
        prompt = f"Explain {user_topic} in 3 bullet points for a 6th semester engineering student."

    # 5. API CALL: Send the selected prompt to the Llama-3 model
    completion = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "system", "content": "You are a GATE Exam expert. Give technical, accurate answer."},
        {"role":"user","content":prompt}],
    )

    # 6. OUTPUT: Print the AI's response to the terminal
    print("\n" + completion.choices[0].message.content)