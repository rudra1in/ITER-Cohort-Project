
from typing import TypedDict, List, Dict, Any


class AgentState(TypedDict, total=False):
    problem: str
    approach: str
    code: str
    language: str
    retrieved_knowledge: List[str]

    intro: str
    analysis: str
    complexity: str
    evaluation: str
    feedback: str
    hint: str
    encouragement: str

    scorecard: Dict[str, int]
    score_history: List[int]
    score: int
    avg_score: float
    done: bool
    test_results: Dict[str, Any]
