import streamlit as st
from groq import Groq
import json

# ==========================================
# 1. إعدادات الصفحة المتقدمة للاستوديوهات
# ==========================================
st.set_page_config(page_title="CampaignOS | Studio Pipeline", page_icon="🎬", layout="wide")

# ==========================================
# 2. حقن تصميم CSS (Dark Studio UI)
# ==========================================
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Tajawal:wght@400;700;900&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Tajawal', sans-serif;
        direction: rtl;
        text-align: right;
    }
    .stApp {
        background-color: #050505;
        background-image: radial-gradient(circle at 50% 0%, #1a1a2e 0%, #050505 80%);
    }
    .hero-title {
        font-size: 3.8rem;
        font-weight: 900;
        background: -webkit-linear-gradient(45deg, #00F2FE, #4FACFE);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        margin-bottom: 0px;
        letter-spacing: -1px;
    }
    .hero-subtitle {
        text-align: center;
        color: #8B9BB4;
        font-size: 1.3rem;
        margin-bottom: 40px;
    }
    .stButton>button {
        background: linear-gradient(90deg, #00F2FE 0%, #4FACFE 100%);
        color: #000;
        border: none;
        border-radius: 6px;
        padding: 15px;
        font-size: 1.3rem;
        font-weight: 900;
        text-transform: uppercase;
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        transform: scale(1.02);
        box-shadow: 0 10px 25px rgba(0, 242, 254, 0.4);
    }
    .metric-card {
        background: rgba(255,255,255,0.03);
        border: 1px solid rgba(255,255,255,0.08);
        border-radius: 8px;
        padding: 25px;
        margin-bottom: 20px;
    }
    div[data-testid="stSidebar"] {
        background-color: #0A0A0F;
        border-left: 1px solid rgba(255,255,255,0.05);
    }
</style>
""", unsafe_allow_html=True)

# ==========================================
# 3. الشريط الجانبي (Studio Settings)
# ==========================================
with st.sidebar:
    st.markdown("### 🎛️ لوحة تحكم الاستوديو")
    API_KEY = st.text_input("🔑 مفتاح Groq API:", type="password")
    st.markdown("---")
    st.markdown("💡 **توجيه المخرج:** صِف المنتج، العميل المستهدف (مثال: شركة إلكترونيات، علامة طبية/مكملات، أو سيارات)، والمدة الزمنية المطلوبة للإعلان.")

st.markdown('<h1 class="hero-title">CampaignOS 🎬</h1>', unsafe_allow_html=True)
st.markdown('<p class="hero-subtitle">محرك الذكاء الاصطناعي لهندسة الحملات الإعلانية السينمائية وعروض الـ CGI الكبرى</p>', unsafe_allow_html=True)

if API_KEY:
    client = Groq(api_key=API_KEY)

    # placeholder مصمم خصيصاً ليتناسب مع مستوى الاحتراف العالي (CGI/Products/Cinematic)
    user_skill = st.text_area(
        "📝 أدخل الـ Brief (موجز المشروع):", 
        placeholder="مثال: أريد بناء مقترح لحملة إعلانية CGI بالكامل لإطلاق شاشة تلفزيون ذكي بتقنية متطورة. الإعلان يجب أن يكون سينمائياً، يركز على المشاهد التشريحية الداخلية (Exploded views) لإبراز قوة المعالج، واستعراض أداء الـ 4K، مع تسعير لشركة إلكترونيات كبرى...",
        height=140
    )

    if st.button("🎬 توليد المعالجة السينمائية (Pitch Deck)", use_container_width=True):
        if user_skill:
            with st.spinner("🎞️ يتم الآن بناء الستوري بورد، هندسة الـ Pipeline، وتسعير المشروع... يرجى الانتظار."):
                
                # ==========================================
                # 4. محرك المخرج السينمائي (The Director Prompt)
                # ==========================================
                prompt = f"""
                أنت الآن تعمل كـ (Executive Creative Director) و (CGI Pipeline Technical Director) في استوديو إعلانات عالمي في هوليوود.
                مهمتك بناء مقترح حملة إعلانية سينمائية شاملة (Pitch Deck) بناءً على هذا الموجز: {user_skill}
                
                يجب أن يكون الرد حصرياً بصيغة JSON وفق هذا الهيكل المعقد (باللغة العربية الفصحى وبمصطلحات تقنية فنية دقيقة):
                {{
                    "creative_treatment": {{
                        "campaign_title": "اسم ملحمي للحملة",
                        "core_concept": "الفكرة الجوهرية (في سطرين)",
                        "visual_metaphor": "الاستعارة البصرية (كيف سنعبر عن الفكرة بصرياً؟)",
                        "lighting_and_mood": "هندسة الإضاءة والمزاج (مثال: إضاءة دراماتيكية عالية التباين، ألوان نيون...)"
                    }},
                    "storyboard_sequence": [
                        {{"shot": "1. الافتتاحية (The Hook)", "camera_movement": "حركة الكاميرا", "action": "وصف دقيق لما يحدث في الـ CGI"}},
                        {{"shot": "2. بناء التوتر (The Build-up)", "camera_movement": "حركة الكاميرا", "action": "وصف دقيق لما يحدث"}},
                        {{"shot": "3. الذروة (The Climax / Exploded View)", "camera_movement": "حركة الكاميرا", "action": "وصف دقيق للقطة التقنية"}},
                        {{"shot": "4. الإغلاق (The Packshot)", "camera_movement": "حركة الكاميرا", "action": "اللقطة النهائية للمنتج مع الشعار"}}
                    ],
                    "technical_pipeline": {{
                        "modeling_and_assets": "كيف سيتم بناء المجسمات والخامات؟",
                        "animation_dynamics": "نوع التحريك (مثال: محاكاة سوائل، Geometry Nodes، ديناميكا معقدة)",
                        "rendering_engine": "محرك التصيير المقترح ولماذا؟ (مثال: Cycles للواقعية المفرطة)",
                        "ai_integration": "كيف سنستخدم أدوات الذكاء الاصطناعي (مثل التوليد السريع للخامات أو النماذج المبدئية) لتسريع مسار العمل؟"
                    }},
                    "commercial_proposal": {{
                        "scope_of_work": "نطاق العمل الرسمي (ماذا سنسلم للعميل؟)",
                        "estimated_timeline": "الجدول الزمني للإنتاج بالأسابيع",
                        "budget_tiers": [
                            {{"tier": "الباقة الأساسية (Standard CGI)", "price": "السعر المتوقع بالدولار", "includes": "ماذا تشمل؟"}},
                            {{"tier": "الباقة السينمائية (Premium 4K + Interactive WebGL)", "price": "السعر المتوقع بالدولار", "includes": "ماذا تشمل؟"}}
                        ]
                    }}
                }}
                """
                
                try:
                    chat_completion = client.chat.completions.create(
                        messages=[
                            {"role": "system", "content": "أنت مخرج إبداعي عالمي وخبير CGI. تخرج البيانات بصيغة JSON فقط."},
                            {"role": "user", "content": prompt}
                        ],
                        model="llama-3.3-70b-versatile",
                        temperature=0.8,
                        max_tokens=6500,
                        response_format={"type": "json_object"}
                    )
                    
                    data = json.loads(chat_completion.choices[0].message.content)
                    
                    # ==========================================
                    # 5. عرض النتائج (Studio Pitch Deck)
                    # ==========================================
                    st.success("تم الانتهاء من هندسة ملف المشروع بنجاح! 🏆")
                    
                    tab1, tab2, tab3, tab4 = st.tabs(["👁️ المعالجة البصرية", "🎞️ الستوري بورد", "⚙️ الـ Pipeline التقني", "💼 العرض المالي"])
                    
                    with tab1:
                        st.markdown('<div class="metric-card">', unsafe_allow_html=True)
                        st.markdown(f"## 🎬 {data['creative_treatment']['campaign_title']}")
                        st.markdown("---")
                        st.markdown(f"**🧠 الفكرة الجوهرية:** {data['creative_treatment']['core_concept']}")
                        st.markdown(f"**🌌 الاستعارة البصرية:** {data['creative_treatment']['visual_metaphor']}")
                        st.markdown(f"**💡 الإضاءة والمزاج (Lighting & Mood):** {data['creative_treatment']['lighting_and_mood']}")
                        st.markdown('</div>', unsafe_allow_html=True)
                        
                    with tab2:
                        st.markdown("### 🎥 تسلسل اللقطات (Cinematic Sequence)")
                        for shot in data['storyboard_sequence']:
                            st.markdown('<div class="metric-card">', unsafe_allow_html=True)
                            st.markdown(f"#### 🎬 {shot['shot']}")
                            st.info(f"**📷 حركة الكاميرا:** {shot['camera_movement']}")
                            st.write(f"**⚙️ الأكشن (CGI):** {shot['action']}")
                            st.markdown('</div>', unsafe_allow_html=True)
                                    
                    with tab3:
                        st.markdown('<div class="metric-card">', unsafe_allow_html=True)
                        st.subheader("🛠️ مسار العمل الهندسي (Technical Pipeline)")
                        st.write(f"**🧱 النمذجة والخامات (Assets & Texturing):** {data['technical_pipeline']['modeling_and_assets']}")
                        st.write(f"**🌪️ التحريك والديناميكا (Animation & Dynamics):** {data['technical_pipeline']['animation_dynamics']}")
                        st.success(f"**🖥️ محرك التصيير (Rendering):** {data['technical_pipeline']['rendering_engine']}")
                        st.warning(f"**🤖 تسريع الإنتاج بالـ AI:** {data['technical_pipeline']['ai_integration']}")
                        st.markdown('</div>', unsafe_allow_html=True)
                        
                    with tab4:
                        st.subheader("💼 مقترح العرض التجاري (Commercial Pitch)")
                        st.markdown(f"**📋 نطاق العمل (Scope of Work):** {data['commercial_proposal']['scope_of_work']}")
                        st.markdown(f"**⏱️ الإطار الزمني للإنتاج:** {data['commercial_proposal']['estimated_timeline']}")
                        st.markdown("---")
                        st.markdown("### 💰 هيكل التسعير الاستراتيجي")
                        for tier in data['commercial_proposal']['budget_tiers']:
                            st.markdown('<div class="metric-card">', unsafe_allow_html=True)
                            st.markdown(f"#### 💎 {tier['tier']}")
                            st.success(f"**التكلفة المتوقعة:** {tier['price']}")
                            st.write(f"**المخرجات:** {tier['includes']}")
                            st.markdown('</div>', unsafe_allow_html=True)

                except Exception as e:
                    st.error(f"حدث خطأ أثناء هندسة الملف. يرجى مراجعة الموجز والمحاولة مجدداً. التفاصيل التقنية: {e}")
        else:
            st.warning("يرجى إدخال موجز المشروع (Brief) للبدء في هندسة الحملة.")
else:
    st.info("👈 يرجى إدخال مفتاح Groq API في القائمة الجانبية للبدء.")
