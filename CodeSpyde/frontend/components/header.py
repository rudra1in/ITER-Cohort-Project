import streamlit as st
from typing import Dict, Any

def render_header(problem: Dict[str, Any]):
    """Renders a compact, clean header bar for the active coding problem."""
    if not problem:
        return
        
    pid = problem.get("id", "")
    title = problem.get("title", "")
    diff = problem.get("difficulty", "Easy")
    topic = problem.get("topic", "Arrays")
    pattern = problem.get("pattern", "")
    
    diff_class = "badge-easy" if diff == "Easy" else "badge-medium" if diff == "Medium" else "badge-hard"
    
    pattern_html = f'<span class="dev-badge badge-topic">{pattern}</span>' if pattern else ""
    
    st.markdown(f"""
    <div style="display:flex; align-items:center; gap:0.6rem; flex-wrap:wrap; margin-bottom:0.75rem; border-bottom:1px solid var(--border); padding-bottom:0.6rem;">
        <code style="font-size:0.75rem; color:var(--text-muted); padding:0.1rem 0.3rem; background:var(--bg-surface); border:1px solid var(--border); border-radius:3px;">{pid}</code>
        <h1 style="font-size:1.25rem; font-weight:700; margin:0; padding:0; color:var(--text-main); line-height:1;">{title}</h1>
        <span class="dev-badge {diff_class}">{diff}</span>
        <span class="dev-badge badge-topic">{topic}</span>
        {pattern_html}
    </div>
    """, unsafe_allow_html=True)
