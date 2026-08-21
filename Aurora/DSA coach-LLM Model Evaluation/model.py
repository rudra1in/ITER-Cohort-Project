import os
from dotenv import load_dotenv

from langchain_google_genai import (
    ChatGoogleGenerativeAI,
    GoogleGenerativeAIEmbeddings
)
from langchain_ollama import ChatOllama

# LOAD API KEY
load_dotenv("apikeys.env")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")


# EMBEDDING MODEL (shared across all LLMs)
embeddings = GoogleGenerativeAIEmbeddings(
    model="gemini-embedding-001",
    google_api_key=GEMINI_API_KEY
)

# MODEL 1 — QWEN
qwen_llm = ChatOllama(
    model="qwen2.5-coder:7b",
    temperature=0.2
)

# MODEL 2 — GEMINI (cloud API)
gemini_llm = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash",  
    google_api_key=GEMINI_API_KEY,
    temperature=0.2
)

# MODEL 3 — LLAMA (local via Ollama)
llama_llm = ChatOllama(
    model="llama3.2:latest",
    temperature=0.2
)

# AVAILABLE MODELS
llm = {
    "qwen": qwen_llm,
    "gemini": gemini_llm,
    "llama": llama_llm
}
