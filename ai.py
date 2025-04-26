from google import genai
from dotenv import load_dotenv
import os

load_dotenv(dotenv_path="secret.env")

api_key=os.getenv("API_KEY")

client = genai.Client(api_key=api_key)  
chat = client.chats.create(model="gemini-2.0-flash")

response = chat.send_message_stream(
    "Explain how AI works in a few words"
)
for chunk in response:
    print(chunk.text, end="")

response = chat.send_message_stream("What did I ask in my previous question?")
for message in chat.get_history():
    print(f'role - {message.role}', end =": ")
    print(message.parts[0].text)