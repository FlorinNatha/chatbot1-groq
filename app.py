from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)

while True:
    question = input("User: ")
    if question != "bye":

        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "user",
                    "content": question
                }
            ],
            max_tokens=50,
            temperature=0
        )

        for choice in response.choices:
            print(f"AI: {choice.message.content}")
    else:
        print("AI: Goodbye!")
        break