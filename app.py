import streamlit as st
import pandas as pd
import requests
import json
from datetime import datetime
import os

# ==========================================
# 1. PAGE CONFIG & UI THEME
# ==========================================
st.set_page_config(page_title="StudioFlow | OS", page_icon="🎬", layout="wide")

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;800&display=swap');
    html, body, [class*="css"] { font-family: 'Inter', sans-serif; }
    
    /* Enterprise Dark Theme Customizations */
    .stApp { background-color: #0b0f19; color: #e2e8f0; }
    .stSidebar { background-color: #111827; border-right: 1px solid #1f2937; }
    h1, h2, h3 { color: #f8fafc; font-weight: 800; }
    
    /* Custom Cards */
    .metric-card {
        background-color: #1e293b;
        border: 1px solid #334155;
        border-radius: 8px;
        padding: 20px;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
    }
    .status-badge {
        display: inline-block; padding: 4px 12px; border-radius: 999px; font-size: 0.8rem; font-weight: 600;
    }
    .status-active { background: #065f46; color: #34d399; }
    .status-warning { background: #78350f; color: #fbbf24; }
</style>
""", unsafe_allow_html=True)

# ==========================================
# 2. MOCK DATABASE & SESSION STATE
# ==========================================
def init_db():
    if 'user' not in st.session_state:
        st.session_state.user = None
    if 'projects' not in st.session_state:
        st.session_state.projects = [
            {"id": "PRJ-001", "name": "Cyberpunk Commercial", "phase": "Production", "budget_used": 65, "status": "active"},
            {"id": "PRJ-002", "name": "Deep Space VFX Sequence", "phase": "Pre-production", "budget_used": 15, "status": "active"}
        ]
    if 'assets' not in st.session_state:
        st.session_state.assets = []
    if 'comments' not in st.session_state:
        st.session_state.comments = []

init_db()

# ==========================================
# 3. AI ENGINE (GROK / xAI INTEGRATION)
# ==========================================
def call_grok(prompt, system_prompt="You are an elite VFX & Film Studio AI Assistant."):
    api_key = os.environ.get("XAI_API_KEY")
    if not api_key:
        return "⚠️ Error: XAI_API_KEY environment variable not set."
    
    headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json",
    }
    payload = {
        "model": "grok-2-1212", # Update model name based on current xAI docs
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.4
    }
    
    try:
        response = requests.post("https://api.x.ai/v1/chat/completions", headers=headers, json=payload)
        response.raise_for_status()
        return response.json()['choices'][0]['message']['content']
    except Exception as e:
    # سيطبع لك هذا السطر رد السيرفر بالكامل
    if hasattr(e, 'response') and e.response is not None:
        return f"⚠️ AI Error Details: {e.response.text}"
    return f"⚠️ AI Engine Error: {str(e)}"

# ==========================================
# 4. MODULES (VIEWS)
# ==========================================

def login_view():
    st.markdown("<h1 style='text-align: center; margin-top: 10vh;'>StudioFlow</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #94a3b8;'>Enterprise Production Pipeline</p>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        with st.form("login_form"):
            username = st.text_input("Username")
            role = st.selectbox("Role", ["Admin", "Director", "Artist"])
            submitted = st.form_submit_button("Secure Login", use_container_width=True)
            if submitted and username:
                st.session_state.user = {"name": username, "role": role}
                st.rerun()

def dashboard_view():
    st.title("Executive Dashboard")
    
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("<div class='metric-card'><h3>Active Projects</h3><h2>2</h2></div>", unsafe_allow_html=True)
    with col2:
        st.markdown("<div class='metric-card'><h3>Global Budget Burn</h3><h2>41%</h2></div>", unsafe_allow_html=True)
    with col3:
        st.markdown("<div class='metric-card'><h3>Impending Deadlines</h3><h2 style='color:#fbbf24;'>1 Warning</h2></div>", unsafe_allow_html=True)

    st.subheader("Project Overview")
    df = pd.DataFrame(st.session_state.projects)
    st.dataframe(df, use_container_width=True, hide_index=True)

def projects_view():
    st.title("Project Management")
    
    
    with st.expander("➕ Create New Project"):
        with st.form("new_project"):
            name = st.text_input("Project Name")
            phase = st.selectbox("Initial Phase", ["Pre-production", "Production", "Post-production", "Delivery"])
            budget = st.number_input("Budget Allocation ($)", min_value=0)
            if st.form_submit_button("Initialize Pipeline"):
                new_proj = {"id": f"PRJ-00{len(st.session_state.projects)+1}", "name": name, "phase": phase, "budget_used": 0, "status": "active"}
                st.session_state.projects.append(new_proj)
                st.success("Project Initialized.")
                st.rerun()
                
    st.subheader("Active Pipelines")
    for proj in st.session_state.projects:
        with st.container():
            st.markdown(f"**{proj['id']} - {proj['name']}** | Phase: {proj['phase']}")
            st.progress(proj['budget_used'] / 100, text=f"Budget Burn: {proj['budget_used']}%")
            st.markdown("---")

def assets_view():
    st.title("Asset Management & AI Tagging")
    
    uploaded_file = st.file_uploader("Upload Asset (EXR, MOV, MP4, OBJ)")
    if uploaded_file is not None:
        if st.button("Process & Auto-Tag via Grok"):
            with st.spinner("AI analyzing asset metadata..."):
                # Simulating AI tagging logic
                prompt = f"Generate 5 relevant tags for a VFX asset named: {uploaded_file.name}. Return ONLY comma separated words."
                tags = call_grok(prompt)
                
                new_asset = {
                    "filename": uploaded_file.name,
                    "version": "v01",
                    "tags": tags,
                    "uploaded_by": st.session_state.user['name']
                }
                st.session_state.assets.append(new_asset)
                st.success("Asset ingested and tagged successfully.")
                
    st.subheader("Asset Repository")
    if st.session_state.assets:
        st.table(pd.DataFrame(st.session_state.assets))
    else:
        st.info("Repository is empty.")

def ai_tools_view():
    st.title("Grok AI Creative Suite")
    
    tool = st.selectbox("Select AI Tool", [
        "Script to Storyboard Ideas", 
        "VFX Pipeline Optimizer", 
        "Budget Risk Analyzer"
    ])
    
    context = st.text_area("Input Context (Script snippet, project description, or pipeline issue)")
    
    if st.button("Execute AI Analysis", type="primary"):
        if context:
            with st.spinner("Grok is processing..."):
                if tool == "Script to Storyboard Ideas":
                    sys_prompt = "You are a Master Storyboard Artist. Break down the script into 3 distinct camera shots with lighting and angle notes."
                elif tool == "VFX Pipeline Optimizer":
                    sys_prompt = "You are a Technical Director. Suggest optimization techniques for rendering and compositing based on the user's issue."
                else:
                    sys_prompt = "You are a Studio Financial Analyst. Predict budget risks based on the provided project description."
                
                result = call_grok(context, system_prompt=sys_prompt)
                st.markdown("### AI Output")
                st.info(result)
        else:
            st.warning("Please provide input context.")

def collaboration_view():
    st.title("Studio Comm-Link")
    
    # Simple threaded view
    for comment in st.session_state.comments:
        st.markdown(f"**{comment['author']}** ({comment['role']}) - *{comment['time']}*")
        st.markdown(f"> {comment['text']}")
        st.markdown("---")
        
    with st.form("new_comment"):
        text = st.text_area("Broadcast Message / Feedback")
        if st.form_submit_button("Post Message"):
            if text:
                st.session_state.comments.append({
                    "author": st.session_state.user['name'],
                    "role": st.session_state.user['role'],
                    "time": datetime.now().strftime("%H:%M:%S"),
                    "text": text
                })
                st.rerun()

# ==========================================
# 5. MAIN ROUTER & SIDEBAR
# ==========================================
def main():
    if st.session_state.user is None:
        login_view()
        return

    with st.sidebar:
        st.markdown(f"### 👤 {st.session_state.user['name']}")
        st.caption(f"Role: {st.session_state.user['role']}")
        if st.button("Logout"):
            st.session_state.user = None
            st.rerun()
            
        st.markdown("---")
        st.markdown("### Navigation")
        
        # Menu selection
        menu = ["Dashboard", "Projects", "Assets", "AI Creative Tools", "Collaboration"]
        choice = st.radio("Go to", menu, label_visibility="collapsed")
        
        st.markdown("---")
        st.caption("StudioFlow OS v1.0 | Powered by xAI")

    # Routing
    if choice == "Dashboard": dashboard_view()
    elif choice == "Projects": projects_view()
    elif choice == "Assets": assets_view()
    elif choice == "AI Creative Tools": ai_tools_view()
    elif choice == "Collaboration": collaboration_view()

if __name__ == "__main__":
    main()
