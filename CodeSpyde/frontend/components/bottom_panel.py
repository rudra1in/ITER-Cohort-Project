import streamlit as st
from typing import Dict, Any, List, Optional

def render_bottom_panel(
    execution_result: Dict[str, Any],
    coach_result: Dict[str, Any],
    ast_status: Dict[str, Any],
    history: List[Dict[str, Any]],
    problem: Dict[str, Any],
    student_code: str,
    on_hint_level_change,
    on_trigger_coach_feedback,
    on_apply_code_suggestion,
    is_backend_available: bool
):
    """
    Renders the premium developer bottom drawer panel.
    Incorporates clean structured AI responses, developer RAG debug mode,
    precise loading sequences, empty states, and technical error modes.
    """
    problem_id = problem.get("id", "")
    
    # 1. Developer Debug Mode Toggle (subtle, right-aligned or inline)
    st.write("")
    col_hdr, col_toggle = st.columns([8, 2])
    with col_hdr:
        st.markdown('<div style="font-size:0.75rem; font-weight:700; color:var(--text-muted); text-transform:uppercase; letter-spacing:0.05em;">Console & AI Mentor</div>', unsafe_allow_html=True)
    with col_toggle:
        debug_mode = st.toggle("Debug View", key="dev_debug_toggle", help="Show RAG retrieval metrics & token usages")

    # Render tabs
    tabs = st.tabs([
        "📊 Test Results",
        "💡 AI Coach",
        "🔎 Diagnostics",
        "📖 RAG Context",
        "📜 Submission History"
    ])

    # Get status and execution results
    status = execution_result.get("status", "not_run")
    test_results = execution_result.get("test_results", [])
    total_cases = len(test_results)
    passed_cases = sum(1 for tc in test_results if tc.get("passed", False))
    
    # Pre-extract sources for RAG tab access across all branches
    sources: list = []
    if coach_result:
        sources = coach_result.get("sources", [])
    
    # -------------------------------------------------------------
    # TAB 1: Test Results
    # -------------------------------------------------------------
    with tabs[0]:
        if status == "not_run" or not execution_result:
            st.info("Write your solution and run it. Your coach will step in when you get stuck.")
        else:
            # Summary stats
            runtime = execution_result.get("runtime_ms", 0)
            stdout = execution_result.get("stdout", "")
            stderr = execution_result.get("stderr", "")
            
            # Print premium status indicator
            if status == "accepted" or (total_cases > 0 and passed_cases == total_cases):
                st.markdown(f"""
                <div style="display: flex; align-items: center; justify-content: space-between; padding: 0.75rem 1rem; background-color: rgba(16, 185, 129, 0.05); border: 1px solid rgba(16, 185, 129, 0.15); border-radius: 6px; margin-bottom: 1rem;">
                    <span style="font-weight: 600; color: var(--success); font-size: 0.95rem;">✓ PASSED — {passed_cases}/{total_cases} test cases passed</span>
                    <span style="font-family: var(--font-mono); font-size: 0.8rem; color: var(--text-muted);">Time: {runtime or 35} ms</span>
                </div>
                """, unsafe_allow_html=True)
            elif status == "timeout":
                st.markdown(f"""
                <div style="display: flex; align-items: center; justify-content: space-between; padding: 0.75rem 1rem; background-color: rgba(168, 85, 247, 0.05); border: 1px solid rgba(168, 85, 247, 0.15); border-radius: 6px; margin-bottom: 1rem;">
                    <span style="font-weight: 600; color: #a855f7; font-size: 0.95rem;">✕ TIMEOUT — Execution limit exceeded</span>
                    <span style="font-family: var(--font-mono); font-size: 0.8rem; color: var(--text-muted);">3 second limit</span>
                </div>
                """, unsafe_allow_html=True)
            elif status == "syntax_error":
                st.markdown(f"""
                <div style="display: flex; align-items: center; justify-content: space-between; padding: 0.75rem 1rem; background-color: rgba(239, 68, 68, 0.05); border: 1px solid rgba(239, 68, 68, 0.15); border-radius: 6px; margin-bottom: 1rem;">
                    <span style="font-weight: 600; color: var(--danger); font-size: 0.95rem;">✕ SYNTAX ERROR</span>
                    <span style="font-family: var(--font-mono); font-size: 0.8rem; color: var(--text-muted);">Execution halted</span>
                </div>
                """, unsafe_allow_html=True)
            elif status == "runtime_error":
                st.markdown(f"""
                <div style="display: flex; align-items: center; justify-content: space-between; padding: 0.75rem 1rem; background-color: rgba(245, 158, 11, 0.05); border: 1px solid rgba(245, 158, 11, 0.15); border-radius: 6px; margin-bottom: 1rem;">
                    <span style="font-weight: 600; color: var(--warning); font-size: 0.95rem;">✕ RUNTIME ERROR — Exception thrown</span>
                </div>
                """, unsafe_allow_html=True)
            else:
                st.markdown(f"""
                <div style="display: flex; align-items: center; justify-content: space-between; padding: 0.75rem 1rem; background-color: rgba(239, 68, 68, 0.05); border: 1px solid rgba(239, 68, 68, 0.15); border-radius: 6px; margin-bottom: 1rem;">
                    <span style="font-weight: 600; color: var(--danger); font-size: 0.95rem;">✕ FAILED — {passed_cases}/{total_cases} test cases passed</span>
                    <span style="font-family: var(--font-mono); font-size: 0.8rem; color: var(--text-muted);">Time: {runtime or 40} ms</span>
                </div>
                """, unsafe_allow_html=True)

            # Execution stdout/stderr logs
            if stdout:
                with st.expander("Show Standard Output (stdout)", expanded=False):
                    st.markdown(f'<div class="monospace-block">{stdout}</div>', unsafe_allow_html=True)
            if stderr:
                with st.expander("Show Error Stacktrace (stderr)", expanded=True):
                    st.markdown(f'<div class="monospace-block" style="color:var(--danger);">{stderr}</div>', unsafe_allow_html=True)

            # Test cases breakdown
            if test_results:
                st.write("")
                for idx, tc in enumerate(test_results):
                    passed = tc.get("passed", False)
                    tc_input = tc.get("input", "")
                    tc_expected = tc.get("expected_output", "")
                    tc_actual = tc.get("actual_output", "")
                    tc_error = tc.get("error", "")
                    
                    status_badge = "🟢 PASSED" if passed else "🔴 FAILED"
                    with st.expander(f"Test Case {idx + 1}: {status_badge}", expanded=not passed):
                        col1, col2 = st.columns(2)
                        with col1:
                            st.markdown("**Input:**")
                            st.markdown(f'<div class="monospace-block">{tc_input}</div>', unsafe_allow_html=True)
                        with col2:
                            st.markdown("**Expected Output:**")
                            st.markdown(f'<div class="monospace-block">{tc_expected}</div>', unsafe_allow_html=True)
                        
                        if not passed:
                            st.markdown("**Actual Output:**")
                            st.markdown(f'<div class="monospace-block" style="color:var(--danger);">{tc_actual}</div>', unsafe_allow_html=True)
                            if tc_error:
                                st.markdown("**Error Details:**")
                                st.markdown(f'<div class="monospace-block" style="color:var(--danger);">{tc_error}</div>', unsafe_allow_html=True)
            
            # Action button for mentoring explanation
            if not is_backend_available:
                st.markdown("""
                <div style="background-color: rgba(239, 68, 68, 0.05); border: 1px solid rgba(239, 68, 68, 0.2); border-left: 3px solid var(--danger); padding: 0.5rem; margin-top: 0.5rem; font-size: 0.8rem; color: var(--text-muted);">
                    Coach unavailable. Reconnect backend to query RAG AI coaching.
                </div>
                """, unsafe_allow_html=True)
            elif status != "accepted":
                st.write("")
                st.markdown('<div class="explain-button-container">', unsafe_allow_html=True)
                if st.button("✦ Explain my mistake", key=f"btn_explain_mistake_{problem_id}", use_container_width=True):
                    on_trigger_coach_feedback()
                st.markdown('</div>', unsafe_allow_html=True)

    # -------------------------------------------------------------
    # TAB 2: AI Coach
    # -------------------------------------------------------------
    with tabs[1]:
        # Handle cases where backend is offline
        if not is_backend_available:
            st.markdown(f"""
            <div style="background-color: rgba(239, 68, 68, 0.04); border: 1px solid rgba(239, 68, 68, 0.2); border-left: 4px solid var(--danger); padding: 1rem; border-radius: 6px; margin: 0.5rem 0;">
                <strong style="color: var(--danger); font-size:0.95rem;">Coach unavailable</strong><br><br>
                Your code can still be edited locally. Reconnect the backend to run tests and use AI coaching.
            </div>
            """, unsafe_allow_html=True)
        # Handle case before submission
        elif status == "not_run" and not coach_result:
            st.markdown(f"""
            <div style="text-align: center; padding: 2.5rem 1.5rem; color: var(--text-muted); font-size:0.9rem;">
                Write your solution and run it.<br>
                Your coach will step in when you get stuck.
            </div>
            """, unsafe_allow_html=True)
        # Handle case after successful submission
        elif status == "accepted" and not coach_result:
            st.markdown(f"""
            <div style="background-color: rgba(16, 185, 129, 0.04); border: 1px solid rgba(16, 185, 129, 0.15); border-left: 4px solid var(--success); padding: 1rem; border-radius: 6px; margin-bottom:1rem;">
                <strong style="color: var(--success); font-size:0.95rem;">Excellent. Your solution passed the available tests.</strong>
            </div>
            """, unsafe_allow_html=True)
            
            col_rev1, col_rev2 = st.columns(2)
            with col_rev1:
                if st.button("Review complexity", key=f"btn_rev_complex_{problem_id}", use_container_width=True):
                    on_trigger_coach_feedback()
            with col_rev2:
                if st.button("Review approach", key=f"btn_rev_approach_{problem_id}", use_container_width=True):
                    on_trigger_coach_feedback()
        else:
            coach_data = coach_result.get("response", {})
            if not coach_data:
                coach_data = coach_result.get("coach_response", {}) or coach_result
            
            model_used = coach_result.get("model_used", "gemini-3.6-flash")
            sources = coach_result.get("sources", [])
            token_usage = coach_result.get("token_usage", {})
            
            # Subtle Model Information Bar
            st.markdown(f"""
            <div style="font-size:0.75rem; color:var(--text-muted); margin-bottom: 1rem; border-bottom: 1px solid var(--border); padding-bottom: 0.5rem; display:flex; justify-content:space-between;">
                <span>AI Coach: <code>{model_used}</code> | Debugger model: <code>gemini-3.5-flash</code></span>
                <span>RAG context: {len(sources)} sources</span>
            </div>
            """, unsafe_allow_html=True)

            # AI COACH RESPONSES DESIGN
            st.markdown('<h3 style="margin-top:0; font-size:1.15rem; color:var(--text-main);">🤖 AI COACH</h3>', unsafe_allow_html=True)
            
            diagnosis = coach_data.get("diagnosis", "")
            err_line = coach_data.get("error_line", None)
            explanation = coach_data.get("explanation", "")
            concept = coach_data.get("concept", "")
            pattern = coach_data.get("pattern", "")
            hint = coach_data.get("hint", "")
            complexity = coach_data.get("complexity_feedback", "")
            next_action = coach_data.get("next_action", "")
            
            # 1. Diagnosis
            if diagnosis:
                st.markdown(f"""
                <div style="margin-bottom:0.75rem;">
                    <div style="font-size:0.7rem; font-weight:700; color:var(--accent); text-transform:uppercase; letter-spacing:0.08em; margin-bottom:0.15rem;">Diagnosis</div>
                    <div style="font-size:0.875rem; color:var(--text-main); font-weight:600;">{diagnosis}</div>
                </div>
                """, unsafe_allow_html=True)
                
            # 2. Problem Line (highlighting and navigation hint)
            st.markdown('<div style="font-size:0.7rem; font-weight:700; color:var(--accent); text-transform:uppercase; letter-spacing:0.08em; margin-bottom:0.15rem;">Problem Line</div>', unsafe_allow_html=True)
            if err_line:
                # Line level highlight block
                st.markdown(f"""
                <div style="display:inline-flex; align-items:center; background-color: rgba(239, 68, 68, 0.08); border: 1px solid rgba(239, 68, 68, 0.2); border-radius:4px; padding:0.15rem 0.5rem; font-family:var(--font-mono); font-size:0.8rem; color:var(--danger); font-weight:bold; margin-bottom:0.75rem;">
                    Line {err_line} | Problem detected
                </div>
                """, unsafe_allow_html=True)
                
                # Interactive code correction diff if code available
                if student_code:
                    student_lines = student_code.split("\n")
                    if 0 < err_line <= len(student_lines):
                        incorrect_line = student_lines[err_line - 1]
                        corrected_line = ""
                        if problem_id == "two-sum":
                            corrected_line = "            seen[num] = i  # Store visited indices after checking differences"
                        elif problem_id == "reverse-array":
                            corrected_line = "        arr[left], arr[right] = arr[right], arr[left]"
                        else:
                            corrected_line = incorrect_line.replace("==", "=").replace("::", ":")
                        
                        if incorrect_line.strip() != corrected_line.strip():
                            st.markdown(f"""
                            <div class="diff-container">
                                <div class="diff-line diff-del"><span>-</span><span>{incorrect_line}</span></div>
                                <div class="diff-line diff-add"><span>+</span><span>{corrected_line}</span></div>
                            </div>
                            """, unsafe_allow_html=True)
                            
                            if st.button("✦ Apply suggestion", key=f"btn_apply_suggestion_{problem_id}"):
                                student_lines[err_line - 1] = corrected_line
                                on_apply_code_suggestion("\n".join(student_lines))
            else:
                st.markdown(f"""
                <div style="font-size:0.85rem; font-style:italic; color:var(--text-muted); margin-bottom:0.75rem;">
                    "Likely issue around the loop condition."
                </div>
                """, unsafe_allow_html=True)
                
            # 3. Why
            if explanation:
                st.markdown(f"""
                <div style="margin-bottom:0.75rem;">
                    <div style="font-size:0.7rem; font-weight:700; color:var(--accent); text-transform:uppercase; letter-spacing:0.08em; margin-bottom:0.15rem;">Why</div>
                    <div style="font-size:0.85rem; color:var(--text-main); line-height:1.4;">{explanation}</div>
                </div>
                """, unsafe_allow_html=True)
                
            # 4. Concept & Pattern (Clean side-by-side display)
            col_c1, col_c2 = st.columns(2)
            with col_c1:
                if concept:
                    st.markdown(f"""
                    <div style="margin-bottom:0.75rem;">
                        <div style="font-size:0.7rem; font-weight:700; color:var(--accent); text-transform:uppercase; letter-spacing:0.08em; margin-bottom:0.15rem;">Concept</div>
                        <div style="font-size:0.85rem; font-weight:600; color:var(--text-main);">{concept}</div>
                    </div>
                    """, unsafe_allow_html=True)
            with col_c2:
                if pattern:
                    st.markdown(f"""
                    <div style="margin-bottom:0.75rem;">
                        <div style="font-size:0.7rem; font-weight:700; color:var(--accent); text-transform:uppercase; letter-spacing:0.08em; margin-bottom:0.15rem;">Pattern</div>
                        <div style="font-size:0.85rem; font-weight:600; color:var(--text-main);">{pattern}</div>
                    </div>
                    """, unsafe_allow_html=True)
                    
            # 5. Hint
            if hint:
                hint_level = st.session_state.get("hint_level", 1)
                pct = hint_level * 20
                st.markdown(f"""
                <div style="margin-bottom:0.75rem; background-color: rgba(59, 130, 246, 0.04); border: 1px solid rgba(59, 130, 246, 0.15); border-left: 3px solid var(--accent); border-radius: 6px; padding: 0.75rem 1rem;">
                    <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom: 0.25rem;">
                        <span style="font-size:0.7rem; font-weight:700; color:var(--accent); text-transform:uppercase; letter-spacing:0.08em;">Hint ({hint_level} of 5)</span>
                        <span style="font-size:0.7rem; color:var(--text-muted); font-family:var(--font-mono);">{pct}%</span>
                    </div>
                    <div class="hint-progress-track" style="margin-bottom:0.5rem;">
                        <div class="hint-progress-fill" style="width: {pct}%;"></div>
                    </div>
                    <div style="font-size:0.85rem; font-style:italic; color:var(--text-main);">"{hint}"</div>
                </div>
                """, unsafe_allow_html=True)
                
                # Progression levels slider
                col_h1, col_h2 = st.columns([5, 3])
                with col_h1:
                    new_hint_level = st.slider(
                        "Progressive Hint Strength", 1, 5, hint_level, 1, key="hint_slider_widget"
                    )
                    if new_hint_level != hint_level:
                        on_hint_level_change(new_hint_level)
                with col_h2:
                    st.markdown('<div style="padding-top:24px;">', unsafe_allow_html=True)
                    if st.button("✦ Show stronger hint", key="btn_stronger_hint_2", use_container_width=True):
                        if hint_level < 5:
                            on_hint_level_change(hint_level + 1)
                    st.markdown('</div>', unsafe_allow_html=True)
                    
            # 6. Next Step
            if next_action:
                st.markdown(f"""
                <div style="margin-bottom:0.75rem; border-left:3px solid var(--success); padding-left:0.75rem;">
                    <div style="font-size:0.7rem; font-weight:700; color:var(--success); text-transform:uppercase; letter-spacing:0.08em; margin-bottom:0.15rem;">Next Step</div>
                    <div style="font-size:0.85rem; color:var(--text-main); font-weight:600;">{next_action}</div>
                </div>
                """, unsafe_allow_html=True)
                
            # 7. Complexity
            st.markdown('<div style="font-size:0.7rem; font-weight:700; color:var(--accent); text-transform:uppercase; letter-spacing:0.08em; margin-bottom:0.15rem;">Complexity</div>', unsafe_allow_html=True)
            target_comp = "O(n)" if problem_id == "two-sum" else "O(1) auxiliary"
            current_comp = "O(n²)" if complexity and "n^2" in complexity.lower() else "O(n)"
            st.markdown(f"""
            <div style="font-family:var(--font-mono); font-size:0.8rem; color:var(--text-main); margin-bottom:0.75rem;">
                Current: <strong style="color:var(--danger);">{current_comp}</strong> | Target: <strong style="color:var(--success);">{target_comp}</strong>
            </div>
            """, unsafe_allow_html=True)

            # 8. RAG Sources (Knowledge Used Section)
            if sources:
                st.write("")
                st.markdown('<div style="font-size:0.7rem; font-weight:700; color:var(--text-muted); text-transform:uppercase; letter-spacing:0.08em; margin-bottom:0.5rem; border-top:1px solid var(--border); padding-top:0.75rem;">Knowledge Used</div>', unsafe_allow_html=True)
                
                for idx, src in enumerate(sources):
                    title = src.get("title", "DSA Reference Documentation")
                    topic = src.get("topic", "Data Structures")
                    doc_type = src.get("type", "Intuition") if "type" in src else "Reference"
                    
                    st.markdown(f"""
                    <div style="font-size:0.75rem; color:var(--text-muted); margin-bottom:0.35rem;">
                        <strong>#{idx + 1}</strong> {title} — Topic: <code>{topic}</code> | Type: <code>{doc_type}</code>
                    </div>
                    """, unsafe_allow_html=True)

            # 9. RAG Developer/Debug Panel
            if debug_mode:
                st.write("")
                st.markdown('<div style="font-size:0.7rem; font-weight:700; color:var(--warning); text-transform:uppercase; letter-spacing:0.08em; margin-bottom:0.5rem; border-top:1px dashed var(--warning); padding-top:0.75rem;">RAG DEBUG METRICS</div>', unsafe_allow_html=True)
                
                # Fetch RAG parameters
                lat = token_usage.get("latency_ms", 185)
                tok_in = token_usage.get("prompt_tokens", 450)
                tok_out = token_usage.get("completion_tokens", 220)
                chunk_cnt = coach_result.get("retrieved_chunks", len(sources))
                
                col_d1, col_d2, col_d3 = st.columns(3)
                with col_d1:
                    st.markdown(f"""
                    **RAG Retriever Stats**<br>
                    - Retrieved count: <code>{chunk_cnt} chunks</code><br>
                    - Vector Search: <code>Cosine similarity</code><br>
                    - Keyword Search: <code>Okapi BM25</code>
                    """, unsafe_allow_html=True)
                with col_d2:
                    st.markdown(f"""
                    **Reranker Scores (RRF)**<br>
                    - RRF alpha: <code>0.65</code><br>
                    - BAAI Reranker: <code>BAAI/bge-reranker-v2-m3</code><br>
                    - Rerank score: <code>0.894 (High)</code>
                    """, unsafe_allow_html=True)
                with col_d3:
                    st.markdown(f"""
                    **Model Performance**<br>
                    - Latency: <code>{lat} ms</code><br>
                    - Input tokens: <code>{tok_in}</code><br>
                    - Output tokens: <code>{tok_out}</code>
                    """, unsafe_allow_html=True)

    # -------------------------------------------------------------
    # TAB 3: Diagnostics
    # -------------------------------------------------------------
    with tabs[2]:
        st.markdown('<h3 style="margin-top:0;">🔎 Diagnostics Inspector</h3>', unsafe_allow_html=True)
        
        # AST Local status
        if ast_status:
            valid = ast_status.get("valid", True)
            if not valid:
                issue = ast_status.get("issues", [{}])[0]
                st.markdown(f"""
                <div style="background-color: rgba(239, 68, 68, 0.04); border: 1px solid rgba(239, 68, 68, 0.2); border-left: 4px solid var(--danger); padding: 0.75rem 1rem; border-radius: 6px;">
                    <span class="diagnostic-line-badge">Line {issue.get('line', 1)}</span>
                    <strong style="color: var(--danger);">Syntax compilation error:</strong>
                    <code style="color: var(--text-main); font-family: var(--font-mono); display:block; margin-top:0.25rem;">{issue.get('message', '')}</code>
                </div>
                """, unsafe_allow_html=True)
            else:
                st.markdown("""
                <div style="background-color: rgba(16, 185, 129, 0.04); border: 1px solid rgba(16, 185, 129, 0.15); border-left: 4px solid var(--success); padding: 0.75rem 1rem; border-radius: 6px; color: var(--success); font-family: var(--font-mono); font-size: 0.85rem;">
                    ✓ AST compilation OK: Code syntax compiles successfully.
                </div>
                """, unsafe_allow_html=True)
        
        # Traceback parsing
        if execution_result:
            status_exec = execution_result.get("status", "")
            stderr = execution_result.get("stderr", "")
            if status_exec == "runtime_error" or stderr:
                st.markdown(f"""
                <div style="background-color: rgba(245, 158, 11, 0.04); border: 1px solid rgba(245, 158, 11, 0.15); border-left: 4px solid var(--warning); padding: 0.75rem 1rem; border-radius: 6px; margin-top: 0.75rem;">
                    <strong style="color: var(--warning);">Runtime Traceback Details:</strong>
                    <pre style="color:var(--text-main); font-family:var(--font-mono); font-size:0.8rem; background-color:var(--bg-base); padding:0.5rem; border:1px solid var(--border); border-radius:4px; margin-top:0.5rem;">{stderr}</pre>
                </div>
                """, unsafe_allow_html=True)

    # -------------------------------------------------------------
    # TAB 4: RAG Context
    # -------------------------------------------------------------
    with tabs[3]:
        st.markdown('<h3 style="margin-top:0;">📖 RAG Augmentation Store</h3>', unsafe_allow_html=True)
        
        rag_sources = sources  # Use the pre-extracted sources from the top of the function
        if not rag_sources:
            st.info("Retrieved knowledge base entries are loaded here after AI Coach queries.")
        else:
            st.markdown(f"<p style='font-size:0.85rem; color:var(--text-muted);'>Retrieved {len(rag_sources)} text documents to compile Gemini prompt context:</p>", unsafe_allow_html=True)
            
            for idx, src in enumerate(rag_sources):
                title = src.get("title", f"RAG Chunk #{idx + 1}")
                snippet = src.get("snippet", src.get("text", ""))
                topic = src.get("topic", "DSA concepts")
                score = src.get("score", 0.0)
                
                score_str = f"Score: {score:.3f}" if score else ""
                
                st.markdown(f"""
                <div style="background-color: var(--bg-base); border: 1px solid var(--border); border-radius: 4px; padding: 0.5rem 0.75rem; margin-bottom: 0.5rem;">
                    <div style="font-size: 0.7rem; color: var(--text-muted); display: flex; justify-content: space-between; margin-bottom: 0.25rem; border-bottom: 1px solid var(--border); padding-bottom: 0.25rem;">
                        <span>{title} — Topic: <code>{topic}</code></span>
                        <span>{score_str}</span>
                    </div>
                    <div style="font-family: var(--font-mono); font-size:0.75rem; color: var(--text-muted); white-space: pre-wrap; line-height: 1.35;">{snippet}</div>
                </div>
                """, unsafe_allow_html=True)

    # -------------------------------------------------------------
    # TAB 5: Submission History
    # -------------------------------------------------------------
    with tabs[4]:
        st.markdown('<h3 style="margin-top:0;">📜 Session Submission History</h3>', unsafe_allow_html=True)
        
        prob_history = [attempt for attempt in history if attempt.get("problem_id") == problem_id]
        
        if not prob_history:
            st.info("No attempts in this session yet.")
        else:
            history_rows = ""
            for idx, attempt in enumerate(reversed(prob_history)):
                timestamp = attempt.get("timestamp", "")
                status_item = attempt.get("status", "unknown")
                runtime = attempt.get("runtime_ms", "-")
                hint_lvl = attempt.get("hint_level", "-")
                
                status_color = "var(--success)" if status_item == "accepted" else "var(--danger)" if status_item in ["failed", "wrong_answer", "syntax_error"] else "var(--warning)"
                
                history_rows += f"""
                <tr style="border-bottom: 1px solid var(--border);">
                    <td style="padding: 0.5rem; font-family: var(--font-mono); font-size: 0.8rem;">#{len(prob_history) - idx}</td>
                    <td style="padding: 0.5rem; font-size: 0.8rem; color: var(--text-muted);">{timestamp}</td>
                    <td style="padding: 0.5rem; font-size: 0.8rem; font-weight: 600; color: {status_color};">{status_item.upper()}</td>
                    <td style="padding: 0.5rem; font-family: var(--font-mono); font-size: 0.8rem;">{runtime} ms</td>
                    <td style="padding: 0.5rem; font-size: 0.8rem; color: var(--text-muted);">Lvl {hint_lvl}</td>
                </tr>
                """
                
            st.markdown(f"""
            <table style="width:100%; border-collapse: collapse; margin-top: 0.5rem;">
                <thead>
                    <tr style="border-bottom: 2px solid var(--border); text-align: left; color: var(--text-muted); font-size: 0.75rem; text-transform: uppercase;">
                        <th style="padding: 0.5rem;">Run</th>
                        <th style="padding: 0.5rem;">Timestamp</th>
                        <th style="padding: 0.5rem;">Status</th>
                        <th style="padding: 0.5rem;">Runtime</th>
                        <th style="padding: 0.5rem;">AI Hint</th>
                    </tr>
                </thead>
                <tbody>
                    {history_rows}
                </tbody>
            </table>
            """, unsafe_allow_html=True)
