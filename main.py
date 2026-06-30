from fastapi import FastAPI
from pydantic import BaseModel
from app import chat

app = FastAPI()

class Message(BaseModel):
    message: str

@app.get('/')
def root():
    return {'status': 'AI Chatbot running'}

@app.post('/chat')
def chat_endpoint(body: Message):
    reply = chat(body.message)
    return {'reply': reply}
