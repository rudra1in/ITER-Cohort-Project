import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.routes import incidents, stream
from backend.vectordb.collections import init_collections
# @app.on_event("startup")
# def startup_db_init():
#     init_collections()
app = FastAPI(
    title="Offline AI Proctor API",
    version="1.0.0",
    description="Local high-performance REST API for offline exam proctoring."
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(stream.router)
app.include_router(incidents.router)

@app.on_event("startup")
def startup_db_init():
    init_collections()

@app.get("/")
def health_check():
    return {
        "status": "ONLINE",
        "mode": "100% Offline Edge Execution"
    }

if __name__ == "__main__":
    uvicorn.run("backend.main:app", host="127.0.0.1", port=8000, reload=True)
