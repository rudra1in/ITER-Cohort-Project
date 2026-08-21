import streamlit as st
from streamlit_ace import st_ace
from frontend.config import DEFAULT_TEMPLATES, EDITOR_THEMES
from frontend.diagnostics import check_syntax_locally
from typing import Dict, Any, Tuple

def render_code_editor(problem: Dict[str, Any]) -> Tuple[str, bool, Dict[str, Any]]:
    """
    Renders the professional IDE editor using streamlit-ace.
    Performs real-time local AST syntax checks.
    Returns a tuple: (current_code, is_valid, ast_diagnostic_details)
    """
    problem_id = problem.get("id", "default")
    
    # Initialize editor themes
    if "editor_theme" not in st.session_state:
        st.session_state.editor_theme = "monokai"
    if "editor_font_size" not in st.session_state:
        st.session_state.editor_font_size = 14
        
    # Get initial code for this problem
    session_code_key = f"code_{problem_id}"
    if session_code_key not in st.session_state:
        st.session_state[session_code_key] = DEFAULT_TEMPLATES.get(problem_id, DEFAULT_TEMPLATES["default"])
        
    # 1. Editor Panel Header
    st.markdown('<div class="dev-panel-header"><span>💻 IDE Code Workspace</span><span style="font-size:0.75rem; color:var(--text-muted);">Python 3.12</span></div>', unsafe_allow_html=True)
    
    # 2. Render Ace Editor
    # Professional dark theme options, active line highlight, font, scroll, etc.
    edited_code = st_ace(
        value=st.session_state[session_code_key],
        language="python",
        theme=st.session_state.editor_theme,
        key=f"ace_editor_widget_{problem_id}",
        font_size=st.session_state.editor_font_size,
        height=380,
        tab_size=4,
        wrap=True,
        show_gutter=True,
        show_print_margin=False,
        auto_update=True
    )
    
    # Update session state with the new edits
    st.session_state[session_code_key] = edited_code

    # 3. Live AST Syntax Checking (Immediate, Local, No API overhead)
    syntax_status = check_syntax_locally(edited_code)
    is_valid = syntax_status["valid"]
    
    if not is_valid:
        issue = syntax_status["issues"][0]
        st.markdown(f"""
        <div class="diagnostic-panel">
            <span class="diagnostic-line-badge">Line {issue['line']}</span>
            <span style="color: var(--danger); font-weight: 600;">{issue['type']}:</span>
            <span style="color: var(--text-main); font-family: var(--font-mono);">{issue['message'].split('|')[-1].strip()}</span>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown(f"""
        <div style="background-color: rgba(16, 185, 129, 0.04); border: 1px solid rgba(16, 185, 129, 0.15); border-left: 3px solid var(--success); border-radius: 4px; padding: 0.5rem; margin-top: 0.5rem; font-family: var(--font-mono); font-size: 0.75rem; color: var(--success); display: flex; align-items: center; gap: 0.5rem;">
            <span>✓</span>
            <span>AST Diagnostics: Syntax compiles without warnings.</span>
        </div>
        """, unsafe_allow_html=True)

    # 4. Keyboard UX Indicator
    st.markdown(
        '<div style="text-align: right; margin-top: 0.25rem; font-size: 0.7rem; color: var(--text-muted);">'
        'Run: <span class="kbd-shortcut">Ctrl+Enter</span> | Submit: <span class="kbd-shortcut">Ctrl+Shift+Enter</span>'
        '</div>',
        unsafe_allow_html=True
    )

    # 5. Compact IDE Toolbar: [ Python 3 ] [Format] [Reset] [Run] [Submit]
    st.write("")
    
    # We lay this out in a single clean row
    col_lang, col_fmt, col_rst, col_run, col_sub = st.columns([2.5, 1.5, 1.5, 2.5, 2.5])
    
    with col_lang:
        # Small language label badge
        st.markdown('<div style="background-color: var(--bg-overlay); border: 1px solid var(--border); border-radius: 6px; padding: 0.35rem; font-family: var(--font-mono); font-size: 0.8rem; text-align: center; font-weight: 600; color: var(--accent);">🐍 Python 3</div>', unsafe_allow_html=True)
        
    with col_fmt:
        format_pressed = st.button("Format", key=f"format_btn_{problem_id}", use_container_width=True)
        
    with col_rst:
        reset_pressed = st.button("Reset", key=f"reset_btn_{problem_id}", use_container_width=True)
        
    with col_run:
        # Run is primary (electric blue accent)
        st.markdown('<div class="run-button-container">', unsafe_allow_html=True)
        run_pressed = st.button("▶ Run Tests", key=f"run_btn_{problem_id}", use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
        
    with col_sub:
        # Submit is secondary but clearly distinguishable (styled differently in CSS)
        submit_pressed = st.button("🚀 Submit", key=f"submit_btn_{problem_id}", use_container_width=True)

    # Handle Reset & Format requests
    if reset_pressed:
        st.session_state[session_code_key] = DEFAULT_TEMPLATES.get(problem_id, DEFAULT_TEMPLATES["default"])
        st.rerun()

    if format_pressed:
        try:
            import black
            formatted = black.format_str(edited_code, mode=black.Mode())
            st.session_state[session_code_key] = formatted
            st.toast("Code Formatted with Black.", icon="✓")
            st.rerun()
        except Exception:
            # Fallback formatting: basic strip of trailing spaces
            lines = edited_code.split("\n")
            cleaned = "\n".join([line.rstrip() for line in lines])
            st.session_state[session_code_key] = cleaned
            st.toast("Spaces formatted.", icon="✓")
            st.rerun()

    # Pass button triggers back to parent
    if run_pressed:
        st.session_state.trigger_run = True
    if submit_pressed:
        st.session_state.trigger_submit = True
        
    return edited_code, is_valid, syntax_status
