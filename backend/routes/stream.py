from fastapi import APIRouter
from backend.schemas.incident import TelemetryPayload

router = APIRouter(prefix="/api/stream", tags=["Telemetry & Stream"])

active_sessions = {}

@router.post("/telemetry")
async def receive_telemetry(payload: TelemetryPayload):
    active_sessions[payload.session_id] = {
        "student_id": payload.student_id,
        "last_timestamp": payload.timestamp,
        "vision_status": payload.vision_data.get("status", "NORMAL"),
        "has_violation": payload.vision_data.get("has_violation", False)
    }
    return {
        "status": "success",
        "session_id": payload.session_id,
        "active_monitors": len(active_sessions)
    }

@router.get("/status/{session_id}")
async def get_session_status(session_id: str):
    session = active_sessions.get(session_id)
    if not session:
        return {"status": "INACTIVE", "message": "No stream data received for session."}
    return {"status": "ACTIVE", "data": session}
