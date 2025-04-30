from fastapi import FastAPI, HTTPException
from google import genai
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import os
from pydantic import BaseModel

load_dotenv(dotenv_path="secret.env")

api_key=os.getenv("API_KEY")

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"],  
)

client = genai.Client(api_key=api_key)  
chat = client.chats.create(model="gemini-2.0-flash")

class Message(BaseModel):
    message: str

#HTTP POST request
@app.post("/chat")
async def chat_with_gemini(msg: Message):
    try:

        user_prompt = f"Summarize this in under 1000 characters and end with a complete sentence: {msg.message}"
        response = chat.send_message_stream(user_prompt)
            
        full_response = ""

        for chunk in response:
            full_response += chunk.text
            
        return {"response":full_response.strip()}

    except Exception as e:
        raise HTTPException(status_code=500, detail="Error communcating with the model")