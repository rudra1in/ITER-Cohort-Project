from typing import Literal

from pydantic import BaseModel, Field


class RunCodeRequest(BaseModel):
    problem_id: str = Field(..., min_length=1)
    language: Literal["java"] = "java"
    code: str = Field(..., min_length=1, max_length=50000)


class TestCaseResult(BaseModel):
    passed: bool
    input: str
    expected: str
    actual: str | None = None
    error: str | None = None


class RunCodeResponse(BaseModel):
    success: bool
    status: Literal[
        "passed",
        "failed",
        "compile_error",
        "runtime_error",
        "timeout",
        "error",
    ]
    results: list[TestCaseResult] = []
    message: str | None = None