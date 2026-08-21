from langgraph.graph import END, START, StateGraph

from src.agents.id_agent import id_agent
from src.agents.video_agent import video_agent
from src.agents.vision_agent import vision_agent
from src.agents.face_embedding_agent import face_embedding_agent
from src.agents.face_verification_agent import face_verification_agent
from src.agents.ledger_agent import ledger_agent
from src.agents.face_storage_agent import face_storage_agent

from src.state import VerificationState


builder = StateGraph(
    VerificationState
)


builder.add_node(
    "id_agent",
    id_agent,
)

builder.add_node(
    "video_agent",
    video_agent,
)

builder.add_node(
    "vision_agent",
    vision_agent,
)

builder.add_node(
    "face_embedding_agent",
    face_embedding_agent,
)

builder.add_node(
    "face_verification_agent",
    face_verification_agent,
)

builder.add_node(
    "ledger_agent",
    ledger_agent,
)

builder.add_node(
    "face_storage_agent",
    face_storage_agent,
)

builder.add_edge(
    START,
    "id_agent",
)

builder.add_edge(
    "id_agent",
    "video_agent",
)

builder.add_edge(
    "video_agent",
    "vision_agent",
)

builder.add_edge(
    "vision_agent",
    "face_embedding_agent",
)

builder.add_edge(
    "face_embedding_agent",
    "face_storage_agent",
)

builder.add_edge(
    "face_storage_agent",
    "face_verification_agent",
)

builder.add_edge(
    "face_verification_agent",
    "ledger_agent",
)

builder.add_edge(
    "ledger_agent",
    END,
)


workflow = builder.compile()