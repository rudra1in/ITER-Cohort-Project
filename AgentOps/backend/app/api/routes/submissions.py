from fastapi import APIRouter, HTTPException

from app.schemas.submission import (
    RunCodeRequest,
    RunCodeResponse,
)

router = APIRouter(
    prefix="/api/submissions",
    tags=["Submissions"],
)


@router.post("/run", response_model=RunCodeResponse)
async def run_code(request: RunCodeRequest):

    if request.language != "java":
        raise HTTPException(
            status_code=400,
            detail="Only Java is currently supported.",
        )

    print("Received submission")
    print("Problem:", request.problem_id)
    print("Language:", request.language)
    print("Code length:", len(request.code))

    # Actual secure execution will be added next.

    return RunCodeResponse(
        success=True,
        status="passed",
        message="Submission received successfully.",
        results=[],
    )