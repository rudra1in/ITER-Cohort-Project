import time
from fastapi import APIRouter, HTTPException
from backend.schemas.incident import IncidentReportRequest, IncidentReportResponse
from backend.vectordb.client import get_chroma_client
from backend.vectordb.embeddings import get_local_embedding_function
from agents.crew import ProctoringCrew

router = APIRouter(prefix="/api/incidents", tags=["Incidents"])

@router.post("/evaluate", response_model=IncidentReportResponse)
async def evaluate_incident(payload: IncidentReportRequest):
    try:
        crew = ProctoringCrew()
        crew_summary = crew.run(
            vision_data=payload.telemetry.vision_data,
            audio_data=payload.telemetry.audio_data
        )

        violations = payload.telemetry.vision_data.get("violations", [])
        if payload.telemetry.audio_data.get("has_speech", False):
            violations.append("Unauthorized Speech Detected")

        verdict = "PASSED"
        score = max(0.0, 100.0 - (len(violations) * 20.0))

        if score < 60.0:
            verdict = "FLAG_FOR_REVIEW"
        elif score < 90.0:
            verdict = "WARNING"

        client = get_chroma_client()
        embedding_fn = get_local_embedding_function()
        transcripts_col = client.get_or_create_collection(
            name="session_transcripts",
            embedding_function=embedding_fn
        )

        incident_id = f"inc_{payload.session_id}_{int(time.time())}"
        transcripts_col.add(
            documents=[f"Student: {payload.student_id} | Violations: {', '.join(violations)} | Summary: {crew_summary[:200]}"],
            ids=[incident_id],
            metadatas=[{"session_id": payload.session_id, "verdict": verdict}]
        )

        return IncidentReportResponse(
            session_id=payload.session_id,
            student_id=payload.student_id,
            credibility_score=score,
            verdict=verdict,
            rule_violations=violations,
            agent_evaluation_summary=crew_summary
        )

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Incident evaluation failed: {str(e)}")
