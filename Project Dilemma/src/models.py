from langchain_groq import ChatGroq


# Agent reasoning model
agent_llm = ChatGroq(
    model="openai/gpt-oss-20b",
    temperature=0,
)


# Vision model
vision_llm = ChatGroq(
    model="qwen/qwen3.6-27b",
    temperature=0,
)