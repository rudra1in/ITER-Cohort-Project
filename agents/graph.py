
from langgraph.graph import StateGraph, START, END

from agents.state import AgentState
from agents.nodes import (
    retrieve_knowledge,
    coach_submission,
    progress_node,
    motivation_node,
)


graph = StateGraph(AgentState)

graph.add_node("retrieve", retrieve_knowledge)
graph.add_node("coach", coach_submission)
graph.add_node("progress", progress_node)
graph.add_node("motivation", motivation_node)

graph.add_edge(START, "retrieve")
graph.add_edge("retrieve", "coach")
graph.add_edge("coach", "progress")
graph.add_edge("progress", "motivation")
graph.add_edge("motivation", END)

agent = graph.compile()
