import time
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from retrieval import search_and_answer

app = FastAPI(
    title="DSA Coach API",
    description="DSA Coach using Gemini, Qwen, Llama, PostgreSQL and pgvector",
    version="1.0"
)

class QuestionRequest(BaseModel):
    question: str
    mode: str = "semantic"
    top_k: int = 3
    history: list = []

@app.get("/")
def home():
    return {"message": "DSA Coach API is running!"}

@app.post("/ask")
def ask_question(request: QuestionRequest):
    if not request.question.strip():
        raise HTTPException(status_code=400, detail="Question cannot be empty")
    if request.mode not in ["semantic", "hybrid"]:
        raise HTTPException(status_code=400, detail="Mode must be 'semantic' or 'hybrid'")

    try:
        evaluations = []
        for model_name in ["gemini", "qwen", "llama"]:
            start = time.time()
            answer = search_and_answer(
                query=request.question,
                mode=request.mode,
                top_k=request.top_k,
                history=request.history,
                model_name=model_name
            )
            latency = time.time() - start
            evaluations.append({
                "model": model_name,
                "latency": latency,
                "answer": answer
            })

        return {
            "question": request.question,
            "mode": request.mode,
            "top_k": request.top_k,
            "evaluation": evaluations   
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

