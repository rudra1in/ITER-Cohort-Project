import streamlit as st

def inject_custom_styles():
    """Injects high-end, premium dark developer mode CSS into the Streamlit application."""
    css = """
    <style>
    /* Reset & CSS Variables for Modern 2026 Developer Theme */
    :root {
        --bg-base: #09090b;
        --bg-surface: #0e0f12;
        --bg-overlay: #14151b;
        --border: #20222e;
        --border-hover: #2e303e;
        --border-focus: #3b82f6;
        --text-main: #e4e4e7;
        --text-muted: #71717a;
        --accent: #2563eb;
        --accent-hover: #1d4ed8;
        --accent-glow: rgba(37, 99, 235, 0.15);
        --success: #10b981;
        --success-border: rgba(16, 185, 129, 0.2);
        --danger: #ef4444;
        --danger-border: rgba(239, 68, 68, 0.2);
        --warning: #f59e0b;
        --warning-border: rgba(245, 158, 11, 0.2);
        --font-mono: 'JetBrains Mono', 'Fira Code', 'Courier New', monospace;
        --font-sans: 'Inter', system-ui, -apple-system, sans-serif;
    }

    /* Core Layout & Page Overrides to hide default Streamlit branding */
    .stApp {
        background-color: var(--bg-base) !important;
        color: var(--text-main) !important;
        font-family: var(--font-sans) !important;
    }
    
    /* Hide top header anchor link, main menu, deploy button, footer */
    header, footer, #MainMenu, .stAppDeployButton {
        visibility: hidden !important;
        display: none !important;
    }

    /* Clean Block Padding to look like a desktop IDE */
    .block-container {
        padding: 1rem 1.5rem 1.5rem 1.5rem !important;
        max-width: 100% !important;
    }

    /* Global Scrollbars */
    ::-webkit-scrollbar {
        width: 5px;
        height: 5px;
    }
    ::-webkit-scrollbar-track {
        background: var(--bg-base);
    }
    ::-webkit-scrollbar-thumb {
        background: var(--border);
        border-radius: 2px;
    }
    ::-webkit-scrollbar-thumb:hover {
        background: var(--text-muted);
    }

    /* Streamlit Containers & Column Margins */
    div[data-testid="stVerticalBlock"] > div {
        padding-top: 0px !important;
        padding-bottom: 0px !important;
    }
    
    /* Sidebar Styling */
    section[data-testid="stSidebar"] {
        background-color: var(--bg-surface) !important;
        border-right: 1px solid var(--border) !important;
        width: 290px !important;
    }
    section[data-testid="stSidebar"] div.stVerticalBlock {
        padding: 1.25rem 1rem !important;
    }

    /* CodeMentor Sidebar Logo */
    .sidebar-logo {
        font-size: 1.15rem;
        font-weight: 700;
        letter-spacing: -0.025em;
        color: var(--text-main);
        display: flex;
        align-items: center;
        gap: 0.5rem;
        margin-bottom: 0.15rem;
    }
    .sidebar-sublogo {
        font-size: 0.6rem;
        font-weight: 600;
        letter-spacing: 0.08em;
        color: var(--text-muted);
        text-transform: uppercase;
        margin-bottom: 1.25rem;
    }

    /* Sidebar Navigation Items */
    .sidebar-nav-item {
        display: flex;
        align-items: center;
        padding: 0.45rem 0.65rem;
        border-radius: 4px;
        font-size: 0.8rem;
        font-weight: 500;
        color: var(--text-muted);
        text-decoration: none;
        transition: all 150ms ease;
        margin-bottom: 0.2rem;
    }
    .sidebar-nav-item:hover, .sidebar-nav-item.active {
        color: var(--text-main);
        background-color: var(--bg-overlay);
    }

    /* Cards & Panel Styling */
    .dev-panel {
        background-color: var(--bg-surface) !important;
        border: 1px solid var(--border) !important;
        border-radius: 6px;
        padding: 1rem;
        margin-bottom: 0.75rem;
        transition: border-color 200ms ease, box-shadow 200ms ease;
    }
    .dev-panel:hover {
        border-color: var(--border-hover) !important;
    }
    .dev-panel-header {
        font-size: 0.75rem;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.04em;
        color: var(--text-muted);
        border-bottom: 1px solid var(--border);
        padding-bottom: 0.4rem;
        margin-bottom: 0.75rem;
        display: flex;
        justify-content: space-between;
        align-items: center;
    }

    /* Problem Statement Container */
    .problem-description-container {
        max-height: 60vh;
        overflow-y: auto;
        padding-right: 0.5rem;
        line-height: 1.55;
        font-size: 0.875rem;
    }
    .problem-description-container p {
        margin-bottom: 0.75rem;
    }

    /* Badges & Meta Indicators */
    .dev-badge {
        display: inline-flex;
        align-items: center;
        padding: 0.1rem 0.4rem;
        border-radius: 3px;
        font-size: 0.7rem;
        font-weight: 600;
        font-family: var(--font-mono);
        border: 1px solid var(--border);
    }
    .badge-easy {
        color: var(--success);
        background-color: rgba(16, 185, 129, 0.03);
        border-color: rgba(16, 185, 129, 0.15);
    }
    .badge-medium {
        color: var(--warning);
        background-color: rgba(245, 158, 11, 0.03);
        border-color: rgba(245, 158, 11, 0.15);
    }
    .badge-hard {
        color: var(--danger);
        background-color: rgba(239, 68, 68, 0.03);
        border-color: rgba(239, 68, 68, 0.15);
    }
    .badge-topic {
        color: var(--text-muted);
        background-color: var(--bg-base);
    }

    /* Monospace Content Blocks */
    .monospace-block {
        font-family: var(--font-mono) !important;
        font-size: 0.8rem !important;
        background-color: var(--bg-base) !important;
        border: 1px solid var(--border) !important;
        border-radius: 4px !important;
        padding: 0.6rem 0.75rem !important;
        margin: 0.4rem 0 !important;
        white-space: pre-wrap !important;
        color: #d1d5db !important;
        line-height: 1.35 !important;
    }
    .example-header {
        font-size: 0.7rem;
        font-weight: 600;
        color: var(--text-muted);
        text-transform: uppercase;
        margin-top: 0.6rem;
        letter-spacing: 0.04em;
    }

    /* Streamlit Tab Customizations */
    .stTabs [data-baseweb="tab-list"] {
        background-color: var(--bg-surface) !important;
        border-bottom: 1px solid var(--border) !important;
        gap: 1px !important;
    }
    .stTabs [data-baseweb="tab"] {
        background-color: transparent !important;
        color: var(--text-muted) !important;
        border: none !important;
        border-bottom: 2px solid transparent !important;
        font-weight: 500 !important;
        font-size: 0.8rem !important;
        font-family: var(--font-sans) !important;
        padding: 0.4rem 0.85rem !important;
        transition: color 150ms ease, background-color 150ms ease !important;
    }
    .stTabs [data-baseweb="tab"]:hover {
        color: var(--text-main) !important;
        background-color: var(--bg-overlay) !important;
    }
    .stTabs [aria-selected="true"] {
        color: var(--text-main) !important;
        border-bottom: 2px solid var(--accent) !important;
        font-weight: 600 !important;
    }

    /* Custom Buttons - IDE Style */
    div.stButton > button {
        background-color: var(--bg-overlay) !important;
        color: var(--text-main) !important;
        border: 1px solid var(--border) !important;
        border-radius: 4px !important;
        font-size: 0.8rem !important;
        font-weight: 500 !important;
        padding: 0.35rem 0.75rem !important;
        transition: all 150ms cubic-bezier(0.4, 0, 0.2, 1) !important;
        height: auto !important;
    }
    div.stButton > button:hover {
        border-color: var(--text-muted) !important;
        background-color: var(--bg-surface) !important;
    }
    div.stButton > button:active {
        background-color: var(--bg-base) !important;
    }

    /* Primary CTA buttons like Run & Explain my Mistake */
    div.run-button-container button {
        background-color: var(--accent) !important;
        color: #ffffff !important;
        border: 1px solid var(--accent) !important;
        font-weight: 600 !important;
    }
    div.run-button-container button:hover {
        background-color: var(--accent-hover) !important;
        border-color: var(--accent-hover) !important;
        box-shadow: 0 0 10px var(--accent-glow) !important;
    }
    
    div.explain-button-container button {
        background-color: rgba(37, 99, 235, 0.08) !important;
        color: var(--accent) !important;
        border: 1px solid rgba(37, 99, 235, 0.3) !important;
        font-weight: 600 !important;
    }
    div.explain-button-container button:hover {
        background-color: rgba(37, 99, 235, 0.15) !important;
    }

    /* Live Diagnostics panel styles */
    .diagnostic-panel {
        background-color: rgba(239, 68, 68, 0.03);
        border: 1px solid rgba(239, 68, 68, 0.15);
        border-left: 3px solid var(--danger);
        border-radius: 4px;
        padding: 0.6rem 0.75rem;
        margin-top: 0.5rem;
        font-family: var(--font-mono);
        font-size: 0.75rem;
    }
    .diagnostic-line-badge {
        background-color: var(--danger);
        color: #ffffff;
        padding: 0.08rem 0.3rem;
        border-radius: 2px;
        font-size: 0.7rem;
        font-weight: bold;
        margin-right: 0.4rem;
    }

    /* Custom Code Diff Styling */
    .diff-container {
        font-family: var(--font-mono);
        font-size: 0.75rem;
        border: 1px solid var(--border);
        border-radius: 4px;
        overflow: hidden;
        background-color: var(--bg-base);
        margin: 0.5rem 0;
    }
    .diff-line {
        padding: 0.2rem 0.6rem;
        display: flex;
        gap: 0.4rem;
        line-height: 1.35;
    }
    .diff-del {
        background-color: rgba(239, 68, 68, 0.08);
        color: #f87171;
        border-left: 3px solid var(--danger);
    }
    .diff-add {
        background-color: rgba(16, 185, 129, 0.08);
        color: #34d399;
        border-left: 3px solid var(--success);
    }

    /* AI Coach Progressive Hint Progress Bar */
    .hint-progress-container {
        margin: 0.5rem 0;
    }
    .hint-progress-track {
        background-color: var(--bg-base);
        border-radius: 2px;
        height: 4px;
        overflow: hidden;
        border: 1px solid var(--border);
    }
    .hint-progress-fill {
        background-color: var(--accent);
        height: 100%;
        transition: width 200ms ease;
    }

    /* Responsive Status Flags in Test results */
    .status-flag {
        font-family: var(--font-mono);
        font-size: 0.7rem;
        font-weight: 700;
        padding: 0.1rem 0.4rem;
        border-radius: 3px;
        text-transform: uppercase;
        border: 1px solid transparent;
    }
    .status-passed {
        color: var(--success);
        background-color: rgba(16, 185, 129, 0.04);
        border-color: rgba(16, 185, 129, 0.15);
    }
    .status-failed {
        color: var(--danger);
        background-color: rgba(239, 68, 68, 0.04);
        border-color: rgba(239, 68, 68, 0.15);
    }
    .status-runtime-error {
        color: var(--warning);
        background-color: rgba(245, 158, 11, 0.04);
        border-color: rgba(245, 158, 11, 0.15);
    }
    
    /* Keyboard helper badge */
    .kbd-shortcut {
        font-family: var(--font-mono);
        font-size: 0.65rem;
        color: var(--text-muted);
        background-color: var(--bg-overlay);
        border: 1px solid var(--border);
        border-radius: 2px;
        padding: 0.05rem 0.25rem;
        margin-left: 0.25rem;
    }
    
    /* Shimmer loading dot keyframes */
    .shimmer {
        animation: pulse 1.2s infinite ease-in-out;
    }
    @keyframes pulse {
        0%, 100% { opacity: 0.4; transform: scale(0.9); }
        50% { opacity: 1; transform: scale(1.1); }
    }
    </style>

    <!-- Global Keydown Event Listener for Keyboard UX -->
    <script>
        const targetWindow = window.parent || window;
        targetWindow.document.addEventListener('keydown', function(e) {
            if ((e.ctrlKey || e.metaKey) && !e.shiftKey && e.key === 'Enter') {
                e.preventDefault();
                const buttons = Array.from(parent.document.querySelectorAll('button'));
                const runButton = buttons.find(b => b.textContent.includes('Run Tests') || b.textContent.includes('▶ Run'));
                if (runButton) {
                    runButton.click();
                }
            }
            if ((e.ctrlKey || e.metaKey) && e.shiftKey && e.key === 'Enter') {
                e.preventDefault();
                const buttons = Array.from(parent.document.querySelectorAll('button'));
                const submitButton = buttons.find(b => b.textContent.includes('Submit') || b.textContent.includes('🚀 Submit'));
                if (submitButton) {
                    submitButton.click();
                }
            }
        });
    </script>
    """
    st.markdown(css, unsafe_allow_html=True)
