import streamlit as st
from typing import List, Dict, Any, Optional
from frontend.config import INITIAL_STUDENT_STATS

def render_sidebar(problems: List[Dict[str, Any]]) -> Optional[Dict[str, Any]]:
    """
    Renders the compact developer sidebar with problem browser, filters, and progress.
    Returns the selected problem dictionary or None.
    """
    # 1. Branding
    st.markdown('<div class="sidebar-logo">⚡ CodeMentor</div>', unsafe_allow_html=True)
    st.markdown('<div class="sidebar-sublogo">AI DSA COACH</div>', unsafe_allow_html=True)
    
    # 2. Problem Browser Filters
    st.markdown('<div style="font-size:0.65rem; font-weight:700; color:var(--text-muted); text-transform:uppercase; margin-bottom:0.35rem; letter-spacing:0.04em;">PROBLEM BROWSER</div>', unsafe_allow_html=True)
    
    search_query = st.text_input(
        "Search problems...",
        value="",
        placeholder="Search by title, topic...",
        label_visibility="collapsed"
    )
    
    # Gather distinct values for filters
    difficulties = ["All"] + sorted(set(p.get("difficulty", "") for p in problems if p.get("difficulty")))
    topics = ["All"] + sorted(set(p.get("topic", "") for p in problems if p.get("topic")))
    patterns = ["All"] + sorted(set(p.get("pattern", "") for p in problems if p.get("pattern")))
    
    col1, col2 = st.columns(2)
    with col1:
        selected_diff = st.selectbox("Difficulty", difficulties, label_visibility="collapsed")
    with col2:
        selected_topic = st.selectbox("Topic", topics, label_visibility="collapsed")
        
    selected_pattern = st.selectbox("Pattern", patterns, label_visibility="collapsed")
    
    # Filtering logic
    filtered_problems = []
    for problem in problems:
        if search_query:
            q = search_query.lower()
            if q not in problem.get("title", "").lower() and q not in problem.get("topic", "").lower():
                continue
        if selected_diff != "All" and problem.get("difficulty") != selected_diff:
            continue
        if selected_topic != "All" and problem.get("topic") != selected_topic:
            continue
        if selected_pattern != "All" and problem.get("pattern") != selected_pattern:
            continue
        filtered_problems.append(problem)
        
    st.write("")
    
    # 3. Problem List
    selected_problem = None
    if not filtered_problems:
        st.caption("No problems match your filters.")
    else:
        if "active_problem_id" not in st.session_state:
            st.session_state.active_problem_id = filtered_problems[0]["id"]
            
        for problem in filtered_problems:
            pid = problem["id"]
            title = problem["title"]
            diff = problem["difficulty"]
            
            solved = st.session_state.get(f"solved_{pid}", False)
            diff_dot = "●" if diff == "Easy" else "◆" if diff == "Medium" else "▲"
            diff_color = "var(--success)" if diff == "Easy" else "var(--warning)" if diff == "Medium" else "var(--danger)"
            status_mark = "✓" if solved else ""
            
            # Build a clean label without excessive emoji
            btn_label = f"{diff_dot} {title}"
            if solved:
                btn_label = f"✓ {title}"
            
            if st.button(
                btn_label,
                key=f"sidebar_btn_{pid}",
                use_container_width=True
            ):
                st.session_state.active_problem_id = pid
                st.session_state.hint_level = 1
                # Clear previous results when switching problems
                st.session_state.execution_result = {}
                st.session_state.coach_result = {}
                st.rerun()
                
            if st.session_state.active_problem_id == pid:
                selected_problem = problem
                
        if selected_problem is None and filtered_problems:
            selected_problem = filtered_problems[0]
            
    st.write("---")
    
    # 4. Progress Widget
    st.markdown('<div style="font-size:0.65rem; font-weight:700; color:var(--text-muted); text-transform:uppercase; margin-bottom:0.35rem; letter-spacing:0.04em;">PROGRESS</div>', unsafe_allow_html=True)
    
    solved_keys = [k for k in st.session_state.keys() if k.startswith("solved_") and st.session_state[k]]
    solved_count = len(solved_keys)
    total_count = len(problems)
    pct = int((solved_count / total_count * 100)) if total_count > 0 else 0
    
    st.markdown(f'''
    <div style="display:flex; justify-content:space-between; font-size:0.7rem; color:var(--text-muted); margin-bottom:0.2rem;">
        <span>Solved</span>
        <span>{solved_count}/{total_count}</span>
    </div>
    <div style="background-color:var(--bg-base); border-radius:2px; height:4px; overflow:hidden; border:1px solid var(--border);">
        <div style="background-color:var(--accent); height:100%; width:{pct}%; transition: width 200ms ease;"></div>
    </div>
    ''', unsafe_allow_html=True)
    
    st.write("")
    col_a, col_b = st.columns(2)
    with col_a:
        st.markdown(f'<div style="font-size:0.6rem; color:var(--text-muted); text-transform:uppercase;">Streak</div><div style="font-size:0.95rem; font-weight:700; color:var(--text-main);">{INITIAL_STUDENT_STATS["streak"]}d</div>', unsafe_allow_html=True)
    with col_b:
        st.markdown(f'<div style="font-size:0.6rem; color:var(--text-muted); text-transform:uppercase;">Accuracy</div><div style="font-size:0.95rem; font-weight:700; color:var(--success);">{INITIAL_STUDENT_STATS["accuracy"]}</div>', unsafe_allow_html=True)
    
    return selected_problem
