from app.agents.graph.checkpointer import create_checkpointer


checkpointer = create_checkpointer()
checkpointer.setup()

print("LangGraph checkpoint tables created successfully.")