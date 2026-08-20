"""
Thin compatibility shim.

orchestration logic is in LangGraphOrchestrator.
This module is kept so existing import paths in main.py don't break.
"""

from app.langgraph_orchestrator import (  
LangGraphOrchestrator as InvestigationOrchestrator,
    GraphState,
)