import os

from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    raise RuntimeError("GROQ_API_KEY not found in .env")

llm = ChatGroq(
    model="openai/gpt-oss-20b",
    temperature=0,
)

response = llm.invoke(
    "You are an identity verification assistant. "
    "Reply with exactly: Agent connection successful."
)

print(response.content)