from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage, AIMessage
from dotenv import load_dotenv

load_dotenv()

llm = ChatGroq(
    model='llama-3.1-8b-instant',
    temperature=0.7
)

chat_history = []

def chat(user_message: str) -> str:
    chat_history.append(HumanMessage(content=user_message))
    response = llm.invoke(chat_history)
    chat_history.append(AIMessage(content=response.content))
    return response.content
