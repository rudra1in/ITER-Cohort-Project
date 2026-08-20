from fastapi import APIRouter

from models.schemas import (
    CodeAnalysisRequest,
    CodeAnalysisResponse,
    ExecuteCodeRequest,
    ExecuteCodeResponse,
    TestCaseResult,
)

from services.code_analyzer import (
    analyze_code
)

from services.code_executor import (
    execute_python,
    execute_python_with_tests
)

from config import CODE_EXECUTION_TIMEOUT


router = APIRouter(
    prefix="/api/code",
    tags=["Code"]
)


# =========================================================
# REAL-TIME ANALYSIS
# =========================================================

@router.post(
    "/analyze",
    response_model=CodeAnalysisResponse
)
async def analyze(
    request: CodeAnalysisRequest
):

    result = analyze_code(
        code=request.code,
        language=request.language
    )

    return result


# =========================================================
# RUN CODE
# =========================================================

@router.post(
    "/execute",
    response_model=ExecuteCodeResponse
)
async def execute(
    request: ExecuteCodeRequest
):

    language = (
        request.language
        .strip()
        .lower()
    )

    if language != "python":

        return ExecuteCodeResponse(
            status="unsupported_language",
            stderr=(
                "Python is currently "
                "supported."
            )
        )

    # First check syntax.

    analysis = analyze_code(
        request.code,
        language
    )

    if not analysis["valid"]:

        return ExecuteCodeResponse(
            status="syntax_error",
            stderr=(
                analysis["issues"][0]["message"]
            )
        )

    # If test cases were supplied,
    # execute against them.

    if request.test_cases:

        test_cases = [
            test_case.model_dump()
            for test_case in request.test_cases
        ]

        result = execute_python_with_tests(
            code=request.code,
            test_cases=test_cases,
            timeout=CODE_EXECUTION_TIMEOUT
        )

        return ExecuteCodeResponse(
            status=result["status"],
            test_results=[
                TestCaseResult(**item)
                for item in result[
                    "test_results"
                ]
            ]
        )

    # Otherwise simply run the code.

    result = execute_python(
        code=request.code,
        timeout=CODE_EXECUTION_TIMEOUT
    )

    return ExecuteCodeResponse(
        status=result["status"],
        stdout=result["stdout"],
        stderr=result["stderr"],
        runtime_ms=result["runtime_ms"]
    )