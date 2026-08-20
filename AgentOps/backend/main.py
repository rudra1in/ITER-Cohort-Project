from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.routes.problems import router as problems_router
from app.api.routes.submissions import router as submissions_router
from app.api.routes.coach import router as coach_router


app = FastAPI(
    title="DSA Coach API",
    description="Backend API for the DSA Coach application",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ============================================================
# API ROUTES
# ============================================================

app.include_router(problems_router)
app.include_router(submissions_router)
app.include_router(coach_router)


# ============================================================
# ROOT
# ============================================================

@app.get("/")
def root():
    return {
        "message": "DSA Coach API is running"
    }