import streamlit as st
from typing import Dict, Any

def render_problem_view(problem: Dict[str, Any]):
    """Renders the problem description, constraints, complexity, and examples."""
    if not problem:
        st.warning("Select a problem to begin.")
        return

    # Container with custom CSS to support independent scrollbar
    st.markdown('<div class="problem-description-container">', unsafe_allow_html=True)
    
    # 1. Description Text
    st.markdown("### Description")
    st.markdown(problem.get("description", ""))
    
    # 2. Examples Section
    examples = problem.get("examples", [])
    if examples:
        st.markdown("### Examples")
        for idx, ex in enumerate(examples):
            st.markdown(f'<div class="example-header">Example {idx + 1}</div>', unsafe_allow_html=True)
            
            ex_input = ex.get("input", "")
            ex_output = ex.get("output", "")
            ex_explanation = ex.get("explanation", "")
            
            explanation_html = f'<div style="font-size: 0.8rem; color: var(--text-muted); margin-top: 0.25rem;"><strong>Explanation:</strong> {ex_explanation}</div>' if ex_explanation else ""
            
            st.markdown(f"""
            <div class="monospace-block"><strong>Input:</strong> {ex_input}
<strong>Output:</strong> {ex_output}{explanation_html}</div>
            """, unsafe_allow_html=True)
            
    # 3. Constraints Section
    constraints = problem.get("constraints", "")
    if constraints:
        st.markdown("### Constraints")
        # Format constraints as list or block
        st.markdown(f'<div class="monospace-block" style="font-size: 0.8rem;">{constraints}</div>', unsafe_allow_html=True)
        
    # 4. Expected Complexity (Time & Space)
    complexity = problem.get("complexity", "")
    if complexity:
        st.markdown("### Expected Complexity")
        st.markdown(f'<div class="monospace-block" style="font-size: 0.8rem;">{complexity}</div>', unsafe_allow_html=True)
        
    st.markdown('</div>', unsafe_allow_html=True)
