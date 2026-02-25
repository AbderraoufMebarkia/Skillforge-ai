import streamlit as st
from groq import Groq
import json
from datetime import datetime

# ==========================================
# 1. إعدادات الصفحة (Enterprise Minimalist)
# ==========================================
st.set_page_config(page_title="Studio OS | Enterprise Pipeline", page_icon="⬛", layout="wide")

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;700&family=Tajawal:wght@300;400;700;900&display=swap');
    html, body, [class*="css"] { font-family: 'Inter', 'Tajawal', sans-serif; background-color: #050505; color: #E0E0E0; }
    .stApp { background-color: #050505; }
    .hero-title { font-size: 3.5rem; font-weight: 900; text-transform: uppercase; letter-spacing: 1px; border-bottom: 2px solid #222; padding-bottom: 10px; margin-bottom: 20px; }
    .stage-header { font-size: 1.5rem; color: #FFFFFF; font-weight: 700; background: #111; padding: 15px; border-right: 4px solid #4FACFE; margin-top: 20px; border-radius: 4px; }
    .metric-card { background: #0A0A0A; border: 1px solid #1A1A1A; border-radius: 4px; padding: 20px; margin-top: 10px; }
    .stButton>button { background-color: #FFFFFF; color: #000000; border: none; padding: 12px 24px; font-weight: 900; text-transform: uppercase; transition: all 0.2s; }
    .stButton>button:hover { background-color: #4FACFE; color: #FFFFFF; }
</style>
""", unsafe_allow_html=True)

# ==========================================
# 2. إدارة الحالة واللغات
# ==========================================
if 'projects_archive' not in st.session_state: st.session_state.projects_archive = []
if 'ui_lang' not in st.session_state: st.session_state.ui_lang = "ar"

loc = {
    "ar": {
        "title": "نظام الاستوديو المتكامل", "subtitle": "هندسة خطوط الإنتاج للمشاريع السينمائية والرقمية الضخمة",
        "brief": "موجز المشروع (Project Brief)", "brief_ph": "مثال: حملة إعلانية CGI بالكامل لشاشة i5 Pro، نحتاج تركيز على التفاصيل التشريحية للمعالج...",
        "btn": "هندسة النظام الإنتاجي الشامل", "tab1": "الاستوديو", "tab2": "الأرشيف"
    },
    "en": {
        "title": "STUDIO OS", "subtitle": "Enterprise Production Pipeline Engineering",
        "brief": "Project Brief", "brief_ph": "e.g., Full CGI commercial for i5 Pro TV, focusing on processor exploded views...",
        "btn": "GENERATE MASTER PIPELINE", "tab1": "Studio", "tab2": "Archive"
    }
}
def t(key): return loc[st.session_state.ui_lang][key]

# ==========================================
# 3. الشريط الجانبي
# ==========================================
with st.sidebar:
    st.markdown("### ⚙️ System Config")
    new_lang = st.radio("UI Language", ["ar", "en"], index=0 if st.session_state.ui_lang == "ar" else 1, horizontal=True)
    if new_lang != st.session_state.ui_lang:
        st.session_state.ui_lang = new_lang
        st.rerun()
    API_KEY = st.text_input("Groq API Key", type="password")
    out_lang = st.selectbox("Output Language", ["العربية", "English"])

# ==========================================
# 4. الواجهة الرئيسية والمحرك الخارق
# ==========================================
st.markdown(f'<div class="hero-title">{t("title")}</div>', unsafe_allow_html=True)
st.markdown(f'<div style="color:#888; margin-bottom:40px; font-size:1.2rem;">{t("subtitle")}</div>', unsafe_allow_html=True)

tab_main, tab_archive = st.tabs([t('tab1'), t('tab2')])

with tab_main:
    text_dir = "rtl" if st.session_state.ui_lang == "ar" else "ltr"
    st.markdown(f'<div style="direction: {text_dir};">', unsafe_allow_html=True)
    
    if API_KEY:
        client = Groq(api_key=API_KEY)
        brief = st.text_area(t('brief'), placeholder=t('brief_ph'), height=150)
        
        if st.button(t('btn'), use_container_width=True):
            if brief:
                with st.spinner("جاري بناء هيكل الاستوديو، توزيع المهام، وتخصيص أدوات الذكاء الاصطناعي..."):
                    
                    # 🚀 المحرك المعماري: إجبار الذكاء الاصطناعي على نموذج الـ 7 مراحل
                    prompt = f"""
                    You are an Elite Studio Technical Director and Pipeline Architect.
                    Project Brief: {brief}
                    Target Output Language: {out_lang}
                    
                    You MUST output a highly technical, deeply detailed JSON object based EXACTLY on this 7-stage architectural framework. DO NOT output generic advice. Use industry-standard terms (CGI, VFX, EXR, Version Control, Render Engines).
                    
                    JSON STRUCTURE:
                    {{
                        "project_title": "Epic Project Title",
                        "stage_1_assessment": {{
                            "team_roles": ["Role 1 & Duty", "Role 2 & Duty"],
                            "pain_points_solved": ["Pain 1", "Pain 2"],
                            "storage_architecture": "Details on cloud/local setup for heavy assets"
                        }},
                        "stage_2_workflow": {{
                            "phases": [
                                {{"phase": "Pre-Production", "tasks": ["Task 1", "Task 2"]}},
                                {{"phase": "Production", "tasks": ["Task 1", "Task 2"]}},
                                {{"phase": "Post-Production", "tasks": ["Task 1", "Task 2"]}}
                            ],
                            "gantt_and_deadlines": "How timelines and resource allocation are automatically managed"
                        }},
                        "stage_3_asset_management": {{
                            "heavy_files_handling": "Strategy for EXR, MOV, cache files",
                            "version_control": "How iteration tracking works",
                            "ai_auto_tagging": "How AI categorizes assets"
                        }},
                        "stage_4_collaboration": {{
                            "sync_methods": "Tools for remote artist sync",
                            "review_pipeline": "Frame-accurate video review and markup strategy"
                        }},
                        "stage_5_ai_creative_tools": {{
                            "ai_storyboarding": "How text-to-image AI initiates the vision",
                            "technical_ai_suggestions": "AI for lighting, compositing, or render denoising",
                            "automation": "Routine tasks eliminated by AI"
                        }},
                        "stage_6_delivery_analytics": {{
                            "export_pipeline": "Delivery formats and QC checks",
                            "performance_dashboard": "Metrics tracked (render times, budget burn)"
                        }},
                        "stage_7_growth_integration": {{
                            "software_plugins": "Required integrations (e.g., Blender, Maya, Nuke)",
                            "marketplace_freelance": "Scaling the team dynamically"
                        }}
                    }}
                    """
                    
                    try:
                        chat_completion = client.chat.completions.create(
                            messages=[
                                {"role": "system", "content": "You are a master of strict JSON formatting and high-end studio pipelines."},
                                {"role": "user", "content": prompt}
                            ],
                            model="llama-3.3-70b-versatile",
                            temperature=0.3,
                            max_tokens=7000,
                            response_format={"type": "json_object"}
                        )
                        
                        data = json.loads(chat_completion.choices[0].message.content)
                        
                        # Save to Archive
                        st.session_state.projects_archive.append({
                            "id": datetime.now().strftime("%Y%m%d_%H%M%S"),
                            "name": data['project_title'],
                            "data": data
                        })
                        
                        # 🎨 العرض البصري الاحترافي للمراحل السبعة
                        st.markdown(f"<h2 style='text-align: center; color: #4FACFE;'>{data['project_title']}</h2>", unsafe_allow_html=True)
                        st.markdown("---")
                        
                        col1, col2 = st.columns(2)
                        
                        with col1:
                            st.markdown("<div class='stage-header'>1️⃣ Assessment & Setup</div>", unsafe_allow_html=True)
                            st.markdown("<div class='metric-card'>", unsafe_allow_html=True)
                            st.markdown("**👥 هيكل الفريق:**")
                            for role in data['stage_1_assessment']['team_roles']: st.markdown(f"- {role}")
                            st.markdown(f"**💾 البنية التحتية للتخزين:** {data['stage_1_assessment']['storage_architecture']}")
                            st.markdown("</div>", unsafe_allow_html=True)
                            
                            st.markdown("<div class='stage-header'>3️⃣ File & Asset Management</div>", unsafe_allow_html=True)
                            st.markdown("<div class='metric-card'>", unsafe_allow_html=True)
                            st.markdown(f"**🗄️ إدارة الملفات الضخمة:** {data['stage_3_asset_management']['heavy_files_handling']}")
                            st.markdown(f"**🔄 نظام التحكم بالنسخ (Version Control):** {data['stage_3_asset_management']['version_control']}")
                            st.markdown(f"**🤖 أتمتة التصنيف (AI Tagging):** {data['stage_3_asset_management']['ai_auto_tagging']}")
                            st.markdown("</div>", unsafe_allow_html=True)
                            
                            st.markdown("<div class='stage-header'>5️⃣ AI & Creative Tools</div>", unsafe_allow_html=True)
                            st.markdown("<div class='metric-card'>", unsafe_allow_html=True)
                            st.markdown(f"**🎨 الستوري بورد بالذكاء الاصطناعي:** {data['stage_5_ai_creative_tools']['ai_storyboarding']}")
                            st.markdown(f"**⚙️ المساعد التقني للرندر والإضاءة:** {data['stage_5_ai_creative_tools']['technical_ai_suggestions']}")
                            st.markdown(f"**⚡ الأتمتة:** {data['stage_5_ai_creative_tools']['automation']}")
                            st.markdown("</div>", unsafe_allow_html=True)
                            
                            st.markdown("<div class='stage-header'>7️⃣ Growth & Integration</div>", unsafe_allow_html=True)
                            st.markdown("<div class='metric-card'>", unsafe_allow_html=True)
                            st.markdown(f"**🔌 الإضافات البرمجية المطلوبة:** {data['stage_7_growth_integration']['software_plugins']}")
                            st.markdown(f"**🌍 التوسع والتوظيف:** {data['stage_7_growth_integration']['marketplace_freelance']}")
                            st.markdown("</div>", unsafe_allow_html=True)

                        with col2:
                            st.markdown("<div class='stage-header'>2️⃣ Project Workflow Engine</div>", unsafe_allow_html=True)
                            st.markdown("<div class='metric-card'>", unsafe_allow_html=True)
                            for phase in data['stage_2_workflow']['phases']:
                                st.markdown(f"**{phase['phase']}**")
                                for task in phase['tasks']: st.markdown(f"- *{task}*")
                            st.markdown(f"**📊 الجدولة وإدارة الموارد:** {data['stage_2_workflow']['gantt_and_deadlines']}")
                            st.markdown("</div>", unsafe_allow_html=True)
                            
                            st.markdown("<div class='stage-header'>4️⃣ Real-time Collaboration</div>", unsafe_allow_html=True)
                            st.markdown("<div class='metric-card'>", unsafe_allow_html=True)
                            st.markdown(f"**📡 أدوات المزامنة:** {data['stage_4_collaboration']['sync_methods']}")
                            st.markdown(f"**🎞️ نظام المراجعة الدقيقة (Frame-accurate):** {data['stage_4_collaboration']['review_pipeline']}")
                            st.markdown("</div>", unsafe_allow_html=True)
                            
                            st.markdown("<div class='stage-header'>6️⃣ Delivery & Analytics</div>", unsafe_allow_html=True)
                            st.markdown("<div class='metric-card'>", unsafe_allow_html=True)
                            st.markdown(f"**📦 مسار التسليم (Export Pipeline):** {data['stage_6_delivery_analytics']['export_pipeline']}")
                            st.markdown(f"**📈 لوحة قياس الأداء:** {data['stage_6_delivery_analytics']['performance_dashboard']}")
                            st.markdown("</div>", unsafe_allow_html=True)

                        st.success("🎯 المنصة جاهزة لاستيعاب سير العمل. كل شيء تحت سقف واحد من الفكرة للتسليم النهائي.")
                        
                    except Exception as e:
                        st.error(f"Error / خطأ: {e}")
    else:
        st.warning("Please insert your Groq API Key.")
    st.markdown('</div>', unsafe_allow_html=True)

with tab_archive:
    if not st.session_state.projects_archive:
        st.info("No projects in the archive yet." if st.session_state.ui_lang == 'en' else "لا توجد مشاريع في الأرشيف حالياً.")
    else:
        for proj in reversed(st.session_state.projects_archive):
            with st.expander(f"📁 {proj['name']}"):
                st.download_button(
                    label="Download Pipeline (JSON)",
                    file_name=f"pipeline_{proj['id']}.json",
                    data=json.dumps(proj['data'], indent=4, ensure_ascii=False),
                    key=f"dl_{proj['id']}"
                )
