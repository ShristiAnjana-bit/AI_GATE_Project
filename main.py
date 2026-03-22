import os
from dotenv import load_dotenv
from groq import Groq

# 1. Load the "secret vault" from the .env file
load_dotenv()

# 2. Grab the key from the vault (instead of writing it here)(the environment)
api_key = os.getenv("GROQ_API_KEY")

# 3. Set up the connection
client = Groq(api_key=api_key)

# 3. Create a request (The "Question")
# Move the input OUTSIDE and ABOVE the request
user_topic = input("What GATE topic do you want to learn today? ")

# Now create the request using that topic
completion = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[
        {
            "role": "user",
            "content": f"Explain {user_topic} like I am a 6th semester student. Give me 3 key points for my GATE preparation."
        }
    ],
)
print(completion.choices[0].message.content)
