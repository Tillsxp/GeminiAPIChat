from google import genai
from dotenv import load_dotenv
import os

load_dotenv(dotenv_path="secret.env")

api_key=os.getenv("API_KEY")

client = genai.Client(api_key=api_key)  
chat = client.chats.create(model="gemini-2.0-flash")

msg = input("Ask a question: ")

response = chat.send_message_stream(msg)

full_response = ""

for chunk in response:
    print(chunk.text, end="")

print(full_response)

print("\n")

second_msg = input("Ask a follow-up(be specific): ")

response = chat.send_message_stream(second_msg)

full_response2 = ""

for chunk in response:
    full_response2 += chunk.text

print(full_response2)