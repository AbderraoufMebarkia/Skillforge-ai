import streamlit as st
from groq import Groq
import json
from datetime import datetime

# ==========================================
# 1. إعدادات الصفحة المتقدمة (Studio Minimalist)
# ==========================================
st.set_page_config(page_title="Studio OS | Apex Edition", page_icon="⬛", layout="wide")

# ==========================================
# 2. حقن تصميم CSS (Ultra-Minimalist / Studio Grade)
# ==========================================
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;700&family=Tajawal:wght@300;400;700&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Inter', 'Tajawal', sans-serif;
        background-color: #0A0A0A;
        color: #E0E0E0;
    }
    .stApp {
        background-color: #0A0A0A;
    }
    h1, h2, h3, h4, h5, h6 {
        color: #FFFFFF;
        font-weight: 300;
        letter-spacing: -0.5px;
    }
    .hero-title {
        font-size: 3rem;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 2px;
        border-bottom: 1px solid #333;
        padding-bottom: 10px;
        margin-bottom: 10px;
    }
    .stButton>button {
        background-color: #FFFFFF;
        color: #000000;
        border: 1px solid #FFFFFF;
        border-radius: 2px;
        padding: 10px 20px;
        font-weight: bold;
        text-transform: uppercase;
        transition: all 0.2s ease;
    }
    .stButton>button:hover {
        background-color: #000000;
        color: #FFFFFF;
    }
    .metric-card {
        background: #111111;
        border: 1px solid #222222;
        border-radius: 2px;
        padding: 20px;
        margin-bottom: 15px;
        border-left: 3px solid #555555;
    }
    div[data-testid="stSidebar"] {
        background-color: #050505;
        border-right: 1px solid #222222;
    }
    .lang-toggle { font-size: 0.8rem; color: #888; }
</style>
""", unsafe_allow_html=True)

# ==========================================
# 3. نظام إدارة الحالة (State Management)
# ==========================================
if 'projects_archive' not in st.session_state:
    st.session_state.projects_archive = []
if 'ui_lang' not in st.session_state:
    st.session_state.ui_lang = "ar"

# ==========================================
# 4. قاموس اللغات (Localization Dictionary)
# ==========================================
loc = {
    "ar": {
        "title": "نظام الاستوديو",
        "subtitle": "هندسة وإدارة المشاريع الإبداعية الكبرى",
        "sidebar_title": "إعدادات النظام",
        "api_key": "مفتاح Groq API",
        "ui_lang": "لغة الواجهة / UI Language",
        "out_lang": "لغة التوليد (المخرجات)",
        "custom_steps": "إضافة مراحل مخصصة (اختياري)",
        "custom_steps_help": "مثال: هندسة الصوت، التسويق الفيروسي، استخراج التراخيص...",
        "brief": "موجز المشروع (Brief)",
        "brief_ph": "صف المشروع، الهدف، الميزانية التقريبية، والمعايير المطلوبة...",
        "generate_btn": "توليد هيكل المشروع",
        "tab_new": "مشروع جديد",
        "tab_archive": "الأرشيف والمشاركة",
        "processing": "جاري معالجة البيانات وبناء الهيكل...",
        "success": "تم إنشاء المشروع بنجاح",
        "download": "تحميل المشروع (JSON)",
        "no_projects": "لا توجد مشاريع في الأرشيف حالياً."
    },
    "en": {
        "title": "STUDIO OS",
        "subtitle": "Enterprise Creative Pipeline & Project Engineering",
        "sidebar_title": "System Config",
        "api_key": "Groq API Key",
        "ui_lang": "UI Language / لغة الواجهة",
        "out_lang": "Output Language",
        "custom_steps": "Inject Custom Pipeline Steps",
        "custom_steps_help": "e.g., Sound Design, Viral Marketing, Legal Clearances...",
        "brief": "Project Brief",
        "brief_ph": "Describe the project, objective, estimated budget, and standards...",
        "generate_btn": "Generate Project Architecture",
        "tab_new": "New Project",
        "tab_archive": "Archive & Share",
        "processing": "Processing data and building architecture...",
        "success": "Project generated successfully",
        "download": "Download Project (JSON)",
        "no_projects": "No projects in the archive yet."
    }
}

# اختصار لاستدعاء النصوص حسب اللغة
def t(key): return loc[st.session_state.ui_lang][key]

# ==========================================
# 5. الشريط الجانبي (Sidebar & Config)
# ==========================================
with st.sidebar:
    st.markdown(f"### ⚙️ {t('sidebar_title')}")
    
    # تبديل لغة الواجهة
    new_lang = st.radio(t('ui_lang'), ["ar", "en"], index=0 if st.session_state.ui_lang == "ar" else 1, horizontal=True)
    if new_lang != st.session_state.ui_lang:
        st.session_state.ui_lang = new_lang
        st.rerun()
        
    API_KEY = st.text_input(t('api_key'), type="password")
    st.markdown("---")
    
    output_language = st.selectbox(t('out_lang'), ["العربية", "English"])
    custom_pipeline = st.text_input(t('custom_steps'), help=t('custom_steps_help'))

# ==========================================
# 6. الواجهة الرئيسية (Main Interface)
# ==========================================
st.markdown(f'<div class="hero-title">{t("title")}</div>', unsafe_allow_html=True)
st.markdown(f'<div style="color:#666; margin-bottom:30px;">{t("subtitle")}</div>', unsafe_allow_html=True)

# نظام التبويبات (Tabs for UX)
tab_main, tab_archive = st.tabs([t('tab_new'), t('tab_archive')])

with tab_main:
    if API_KEY:
        client = Groq(api_key=API_KEY)
        
        # تغيير اتجاه النص بناءً على لغة الواجهة
        text_dir = "rtl" if st.session_state.ui_lang == "ar" else "ltr"
        st.markdown(f'<div style="direction: {text_dir};">', unsafe_allow_html=True)
        
        brief = st.text_area(t('brief'), placeholder=t('brief_ph'), height=150)
        
        if st.button(t('generate_btn'), use_container_width=True):
            if brief:
                with st.spinner(t('processing')):
                    
                    # ==========================================
                    # 7. محرك القيود غير المرئية (The Apex Prompt)
                    # ==========================================
                    prompt = f"""
                    You are an Elite Executive Producer and Technical Pipeline Architect at a Tier-1 Hollywood Studio.
                    Project Brief: {brief}
                    Additional Required Pipeline Steps: {custom_pipeline if custom_pipeline else "None"}
                    Target Output Language: {output_language}
                    
                    HIDDEN CONSTRAINTS (MANDATORY):
                    1. Use global enterprise standards (ISO quality management, SMPTE for technicals).
                    2. Tone must be hyper-professional, brutally realistic, and analytical. No marketing fluff.
                    3. Budgets must be realistic for high-end studio work (tier 1: MVP, tier 2: Studio Standard, tier 3: Blockbuster).
                    4. If 'Additional Required Pipeline Steps' are provided, you MUST integrate them logically into the workflow.
                    
                    OUTPUT FORMAT: STRICT JSON EXACTLY matching this structure:
                    {{
                        "executive_summary": {{"project_name": "String", "logline": "String", "core_challenge": "String"}},
                        "technical_pipeline": [
                            {{"phase": "String", "tools_used": "String", "execution_details": "String"}}
                        ],
                        "custom_injected_steps": "Explain how the user's additional steps were integrated",
                        "financial_scoping": [
                            {{"tier": "String", "estimated_cost": "String", "deliverables": "String"}}
                        ],
                        "risk_assessment": ["Risk 1", "Risk 2"]
                    }}
                    """
                    
                    try:
                        chat_completion = client.chat.completions.create(
                            messages=[
                                {"role": "system", "content": "You output strict JSON only."},
                                {"role": "user", "content": prompt}
                            ],
                            model="llama-3.3-70b-versatile",
                            temperature=0.3, # درجة حرارة منخفضة لضمان الدقة والاحترافية والواقعية
                            max_tokens=6000,
                            response_format={"type": "json_object"}
                        )
                        
                        project_data = json.loads(chat_completion.choices[0].message.content)
                        
                        # حفظ في الأرشيف
                        project_entry = {
                            "id": datetime.now().strftime("%Y%m%d_%H%M%S"),
                            "date": datetime.now().strftime("%Y-%m-%d %H:%M"),
                            "name": project_data['executive_summary']['project_name'],
                            "data": project_data
                        }
                        st.session_state.projects_archive.append(project_entry)
                        
                        st.success(t('success'))
                        
                        # عرض البيانات
                        st.markdown(f"## 📄 {project_data['executive_summary']['project_name']}")
                        st.markdown(f"**Logline:** {project_data['executive_summary']['logline']}")
                        
                        st.markdown("### ⚙️ Pipeline")
                        for step in project_data['technical_pipeline']:
                            st.markdown('<div class="metric-card">', unsafe_allow_html=True)
                            st.markdown(f"**{step['phase']}**")
                            st.markdown(f"*Tools:* `{step['tools_used']}`")
                            st.markdown(f"> {step['execution_details']}")
                            st.markdown('</div>', unsafe_allow_html=True)
                            
                        st.markdown("### 💰 Financial Scoping")
                        for tier in project_data['financial_scoping']:
                            st.markdown(f"- **{tier['tier']}** | {tier['estimated_cost']} | *{tier['deliverables']}*")
                            
                    except Exception as e:
                        st.error(f"Error / خطأ: {e}")
        st.markdown('</div>', unsafe_allow_html=True)
    else:
        st.warning("Please enter your API Key in the sidebar / يرجى إدخال مفتاح API في القائمة الجانبية")

# ==========================================
# 8. واجهة الأرشيف والمشاركة (Archive & Share)
# ==========================================
with tab_archive:
    if not st.session_state.projects_archive:
        st.info(t('no_projects'))
    else:
        for proj in reversed(st.session_state.projects_archive):
            with st.expander(f"📁 {proj['name']} - ({proj['date']})"):
                json_string = json.dumps(proj['data'], indent=4, ensure_ascii=False)
                
                # زر تحميل كملف JSON للمشاركة
                st.download_button(
                    label=t('download'),
                    file_name=f"project_{proj['id']}.json",
                    mime="application/json",
                    data=json_string,
                    key=f"dl_{proj['id']}"
                )
                
                # عرض الكود لمراجعته برمجياً
                st.code(json_string, language="json")
