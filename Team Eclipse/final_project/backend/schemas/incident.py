from pydantic import BaseModel
from typing import List, Dict, Any

class TelemetryPayload(BaseModel):
    session_id: str
    student_id: str
    timestamp: float
    vision_data: Dict[str, Any]
    audio_data: Dict[str, Any]

class IncidentReportRequest(BaseModel):
    session_id: str
    student_id: str
    telemetry: TelemetryPayload

class IncidentReportResponse(BaseModel):
    session_id: str
    student_id: str
    credibility_score: float
    verdict: str
    rule_violations: List[str]
    agent_evaluation_summary: str
