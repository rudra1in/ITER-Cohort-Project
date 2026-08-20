from langgraph.graph import StateGraph, START, END

from app.agents.graph.state import CoachState

from app.agents.graph.nodes import (
    memory_node,
    router_node,
    retrieve_node,
    coach_node,
    code_node,
    hint_node,
    interview_node,
    mcq_node,
    roadmap_node,
    evaluate_node,
    conversation_node,
)

from app.agents.graph.checkpointer import create_checkpointer


# ============================================================
# BUILD LANGGRAPH
# ============================================================

builder = StateGraph(CoachState)


# ============================================================
# NODES
# ============================================================

builder.add_node(
    "memory",
    memory_node,
)

builder.add_node(
    "router",
    router_node,
)

builder.add_node(
    "retrieve",
    retrieve_node,
)

builder.add_node(
    "coach",
    coach_node,
)

builder.add_node(
    "code",
    code_node,
)

builder.add_node(
    "hint",
    hint_node,
)

builder.add_node(
    "interview",
    interview_node,
)

builder.add_node(
    "mcq",
    mcq_node,
)

builder.add_node(
    "roadmap",
    roadmap_node,
)

builder.add_node(
    "evaluate",
    evaluate_node,
)

builder.add_node(
    "conversation",
    conversation_node,
)

# ============================================================
# GRAPH FLOW
# ============================================================

# START
#   ↓
# Memory
#   ↓
# Router
#   ↓
# Retrieval
#   ↓
# Coach / Code / Hint
#   ↓
# END

# ============================================================
# START → MEMORY
# ============================================================

builder.add_edge(
    START,
    "memory",
)

# ============================================================
# MEMORY → ROUTER
# ============================================================

builder.add_edge(
    "memory",
    "router",
)

# ============================================================
# ROUTER → RETRIEVAL
# ============================================================

builder.add_edge(
    "router",
    "retrieve",
)

# ============================================================
# ROUTE AGENT
# ============================================================

def route_agent(state: CoachState) -> str:
    """
    Decide which specialized agent should execute
    after RAG retrieval.
    """

    agent_type = state.get(
        "agent_type",
        "coach",
    )

    if agent_type == "code":
        return "code"

    if agent_type == "hint":
        return "hint"

    if agent_type == "interview":
        return "interview"

    if agent_type == "mcq":
        return "mcq"

    if agent_type == "roadmap":
        return "roadmap"

    return "coach"

# ============================================================
# RETRIEVE → SPECIALIZED AGENT
# ============================================================

builder.add_conditional_edges(
    "retrieve",
    route_agent,
    {
        "coach": "coach",
        "code": "code",
        "hint": "hint",
        "interview": "interview",
        "mcq": "mcq",
        "roadmap": "roadmap",
    },
)

# ============================================================
# AGENT → EVALUATION
# ============================================================

builder.add_edge(
    "coach",
    "evaluate",
)

builder.add_edge(
    "code",
    "evaluate",
)

builder.add_edge(
    "hint",
    "evaluate",
)

builder.add_edge(
    "interview",
    "evaluate",
)

builder.add_edge(
    "mcq",
    "evaluate",
)

builder.add_edge(
    "roadmap",
    "evaluate",
)

# ============================================================
# ROUTE AFTER EVALUATION
# ============================================================

def route_after_evaluation(state: CoachState) -> str:
    """
    Decide whether the response should be accepted
    or the agent should retry.

    GOOD:
        → END

    BAD + retries available:
        → selected agent again

    BAD + maximum retries reached:
        → END
    """

    evaluation = state.get(
        "evaluation",
        "good",
    )

    retry_count = state.get(
        "retry_count",
        0,
    )

    max_retries = state.get(
        "max_retries",
        2,
    )

    # --------------------------------------------------------
    # Good response
    # --------------------------------------------------------

    if evaluation == "good":
        return "conversation"

    # --------------------------------------------------------
    # Maximum retry protection
    # --------------------------------------------------------

    if retry_count >= max_retries:
        return "conversation"

    # --------------------------------------------------------
    # Retry selected agent
    # --------------------------------------------------------

    agent_type = state.get(
        "agent_type",
        "coach",
    )

    if agent_type == "code":
        return "code"

    if agent_type == "hint":
        return "hint"

    if agent_type == "interview":
        return "interview"

    if agent_type == "mcq":
        return "mcq"

    if agent_type == "roadmap":
        return "roadmap"

    return "coach"


# ============================================================
# EVALUATE → NEXT STEP
# ============================================================

builder.add_conditional_edges(
    "evaluate",
    route_after_evaluation,
    {
        "conversation": "conversation",
        "coach": "coach",
        "code": "code",
        "hint": "hint",
        "interview": "interview",
        "mcq": "mcq",
        "roadmap": "roadmap",
    },
)

# ============================================================
# CONVERSATION → END
# ============================================================

builder.add_edge(
    "conversation",
    END,
)

# ============================================================
# CREATE CHECKPOINTER
# ============================================================

checkpointer = create_checkpointer()


# ============================================================
# COMPILE GRAPH WITH CHECKPOINTER
# ============================================================

graph = builder.compile(
    checkpointer=checkpointer
)