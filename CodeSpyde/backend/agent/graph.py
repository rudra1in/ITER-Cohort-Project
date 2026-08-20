from __future__ import annotations

import os

from langgraph.graph import (
    START,
    END,
    StateGraph,
)

from agent.state import DSAAgentState
from agent.nodes import (
    load_problem_node,
    memory_node,
    analyze_code_node,
    execute_code_node,
    build_retrieval_query_node,
    retrieve_node,
    rerank_node,
    select_model_node,
    coach_node,
    success_node,
)
from agent.routing import (
    after_analysis,
    after_execution,
)


def build_dsa_coach_graph():

    builder = StateGraph(
        DSAAgentState
    )

    # -------------------------------
    # Nodes
    # -------------------------------

    builder.add_node(
        "load_problem",
        load_problem_node,
    )

    builder.add_node(
        "memory",
        memory_node,
    )

    builder.add_node(
        "analyze",
        analyze_code_node,
    )

    builder.add_node(
        "execute",
        execute_code_node,
    )

    builder.add_node(
        "build_query",
        build_retrieval_query_node,
    )

    builder.add_node(
        "retrieve",
        retrieve_node,
    )

    builder.add_node(
        "rerank",
        rerank_node,
    )

    builder.add_node(
        "model_router",
        select_model_node,
    )

    builder.add_node(
        "coach",
        coach_node,
    )

    builder.add_node(
        "success",
        success_node,
    )

    # -------------------------------
    # Main flow
    # -------------------------------

    builder.add_edge(
        START,
        "load_problem",
    )

    builder.add_edge(
        "load_problem",
        "memory",
    )

    builder.add_edge(
        "memory",
        "analyze",
    )

    # -------------------------------
    # Syntax routing
    # -------------------------------

    builder.add_conditional_edges(
        "analyze",
        after_analysis,
        {
            "coach": "model_router",
            "execute": "execute",
        },
    )

    # -------------------------------
    # Execution routing
    # -------------------------------

    builder.add_conditional_edges(
        "execute",
        after_execution,
        {
            "success": "success",
            "retrieve": "build_query",
            "coach": "model_router",
        },
    )

    # -------------------------------
    # RAG
    # -------------------------------

    builder.add_edge(
        "build_query",
        "retrieve",
    )

    builder.add_edge(
        "retrieve",
        "rerank",
    )

    builder.add_edge(
        "rerank",
        "model_router",
    )

    # -------------------------------
    # LLM
    # -------------------------------

    builder.add_edge(
        "model_router",
        "coach",
    )

    # -------------------------------
    # End
    # -------------------------------

    builder.add_edge(
        "coach",
        END,
    )

    builder.add_edge(
        "success",
        END,
    )

    return builder.compile()


dsa_coach_graph = (
    build_dsa_coach_graph()
)