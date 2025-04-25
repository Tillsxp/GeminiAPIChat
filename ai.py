from google import genai
from dotenv import load_dotenv
import os

load_dotenv(dotenv_path="secret.env")

api_key=os.getenv("API_KEY")

client = genai.Client(api_key=api_key)  

response = client.models.generate_content(
    model="gemini-2.0-flash", contents="Explain how AI works in a few words"
)

print(response.text)