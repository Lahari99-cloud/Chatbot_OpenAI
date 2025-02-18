import os
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables
load_dotenv()

# Fix: Use correct variable name in .env
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

if not OPENAI_API_KEY:
    print("❌ ERROR: Missing OpenAI API Key. Check your .env file!")
    exit()

# Initialize OpenAI client correctly
openai = OpenAI(api_key=OPENAI_API_KEY)

# Chatbot conversation logic
messages = [
    { "role": "system", "content": "You are a sarcastic assistant!" }
]

def chat_bot():
    while True:
        message = input("User: ")
        if message.lower() == "quit":
            break
        messages.append( { "role": "user", "content": message } )
        
        output = openai.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages
        )

        assistant_reply = output.choices[0].message.content
        messages.append({ "role": "assistant", "content": assistant_reply })
        print(assistant_reply)

# Ensure script runs correctly
if __name__ == "__main__":
    chat_bot()
