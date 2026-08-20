from typing import Any, Optional
from pydantic import BaseModel, Field


# ============================================================
# COACH SCHEMA
# ============================================================


class SourceItem(BaseModel):
    """A single RAG source chunk surfaced in the coach response."""
    title: str = ""
    topic: str = ""
    pattern: str = ""
    chunk_type: str = ""
    score: float = 0.0


class CoachAIResponse(BaseModel):
    status: str = "ok"
    diagnosis: str = ""
    explanation: str = ""
    hint: str = ""
    concept: str = ""
    pattern: str = ""
    complexity_feedback: str = ""
    next_action: str = ""
    error_line: Optional[int] = None
    error_type: Optional[str] = None
    hint_level: int = Field(default=1, ge=1, le=5)
    should_show_solution: bool = False
    confidence: float = Field(default=0.0, ge=0.0, le=1.0)
    sources: list[SourceItem] = Field(default_factory=list)



class CoachRequest(BaseModel):
    user_id: str
    problem_id: str
    code: str
    language: str = "python"
    request_type: str = "debug"
    hint_level: int = 1


class CoachResponse(BaseModel):
    status: str
    model_used: str
    response: CoachAIResponse
    retrieved_chunks: int
    sources: list[dict[str, Any]] = []
    token_usage: dict[str, Any] = {}


# ============================================================
# CODE ANALYSIS SCHEMAS
# ============================================================

class CodeIssue(BaseModel):
    line: int
    column: int
    end_line: Optional[int] = None
    end_column: Optional[int] = None
    severity: str
    type: str
    message: str


class CodeAnalysisRequest(BaseModel):
    code: str
    language: str = "python"


class CodeAnalysisResponse(BaseModel):
    valid: bool
    issues: list[CodeIssue] = []
    message: Optional[str] = None


# ============================================================
# CODE EXECUTION SCHEMAS
# ============================================================

class TestCase(BaseModel):
    input: Any
    expected_output: Any


class ExecuteCodeRequest(BaseModel):
    code: str
    language: str = "python"
    test_cases: list[TestCase] = []


class TestCaseResult(BaseModel):
    passed: bool
    input: Any
    expected_output: Any
    actual_output: Any
    error: Optional[str] = None


class ExecuteCodeResponse(BaseModel):
    status: str
    stdout: Optional[str] = None
    stderr: Optional[str] = None
    runtime_ms: Optional[int] = None
    test_results: Optional[list[TestCaseResult]] = None