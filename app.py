import streamlit as st
from groq import Groq
import json

# ==========================================
# 1. إعدادات الصفحة المتقدمة
# ==========================================
st.set_page_config(page_title="SkillForge OS | إمبراطورية المنتجات الرقمية", page_icon="💎", layout="wide")

# ==========================================
# 2. حقن تصميم CSS فاخر (Premium UI)
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
        background-color: #0E1117;
        background-image: radial-gradient(circle at 50% 0%, #1a1f35 0%, #0E1117 70%);
    }
    .hero-title {
        font-size: 3.5rem;
        font-weight: 900;
        background: -webkit-linear-gradient(45deg, #FF6B6B, #FF8E53);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        margin-bottom: 0px;
    }
    .hero-subtitle {
        text-align: center;
        color: #A0AEC0;
        font-size: 1.2rem;
        margin-bottom: 40px;
    }
    .stButton>button {
        background: linear-gradient(90deg, #FF6B6B 0%, #FF8E53 100%);
        color: white;
        border: none;
        border-radius: 8px;
        padding: 15px;
        font-size: 1.2rem;
        font-weight: bold;
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        transform: scale(1.02);
        box-shadow: 0 10px 20px rgba(255, 107, 107, 0.3);
    }
    .metric-card {
        background: rgba(255,255,255,0.05);
        border: 1px solid rgba(255,255,255,0.1);
        border-radius: 10px;
        padding: 20px;
        margin-bottom: 15px;
    }
    div[data-testid="stSidebar"] {
        background-color: #11151C;
        border-left: 1px solid rgba(255,255,255,0.05);
    }
</style>
""", unsafe_allow_html=True)

# ==========================================
# 3. الشريط الجانبي (Sidebar) والهوية
# ==========================================
with st.sidebar:
    st.markdown("### ⚙️ إعدادات المصنع")
    API_KEY = st.text_input("🔑 مفتاح Groq API:", type="password", help="أدخل المفتاح هنا لتشغيل النظام")
    st.markdown("---")
    st.markdown("💡 **نصيحة للمحترفين:** كلما كنت دقيقاً في وصف مهارتك، كلما كانت النتائج التسويقية أكثر تدميراً للمنافسين.")

st.markdown('<h1 class="hero-title">SkillForge OS 💎</h1>', unsafe_allow_html=True)
st.markdown('<p class="hero-subtitle">النظام المتقدم لهندسة المنتجات الرقمية وتحويل المهارات إلى أصول تدر الدخل</p>', unsafe_allow_html=True)

if API_KEY:
    client = Groq(api_key=API_KEY)

    user_skill = st.text_area(
        "🧠 صِف مهارتك أو خبرتك بتفصيل:", 
        placeholder="مثال: أنا مبرمج إضافات بلندر (Addons) ومصمم 3D. أتقن البايثون والـ Geometry Nodes. أريد إطلاق منتج يعلم الناس كيف يبرمجون أدواتهم الخاصة لتسريع عملهم...",
        height=120
    )

    if st.button("🚀 إطلاق محرك الهندسة العكسية", use_container_width=True):
        if user_skill:
            with st.spinner("🔥 يتم الآن تشغيل 4 وكلاء ذكاء اصطناعي (أبحاث، مناهج، تسويق، مبيعات)... يرجى الانتظار."):
                
                # ==========================================
                # 4. محرك الأوامر الخارق (The God-Tier Prompt)
                # ==========================================
                prompt = f"""
                أنت الآن تعمل كوكالة تسويق وهندسة منتجات رقمية عالمية.
                مهمتك تحويل خبرة العميل إلى إمبراطورية رقمية متكاملة.
                
                بيانات العميل وخبرته: {user_skill}
                
                أريد مخرجات باللغة العربية الفصحى الاحترافية والحديثة (بأسلوب تسويقي مقنع وجذاب جداً).
                يجب أن يكون الرد حصرياً بصيغة JSON وفق هذا الهيكل المعقد:
                {{
                    "market_research": {{
                        "avatar": "وصف دقيق لشخصية العميل المحتمل",
                        "deep_pains": ["ألم 1 عميق", "ألم 2", "ألم 3"],
                        "ultimate_desire": "الرغبة النهائية العميقة للعميل"
                    }},
                    "brand_positioning": {{
                        "product_name": "اسم عبقري وجذاب للمنتج",
                        "unique_mechanism": "الآلية الفريدة (كيف يحل هذا الكورس المشكلة بطريقة غير مسبوقة؟)",
                        "grand_promise": "الوعد الكبير (في جملة واحدة قوية)"
                    }},
                    "course_curriculum": [
                        {{"module": "اسم الوحدة 1", "objective": "الهدف من الوحدة", "lessons": ["الدرس 1", "الدرس 2", "الدرس 3"]}},
                        {{"module": "اسم الوحدة 2", "objective": "الهدف من الوحدة", "lessons": ["الدرس 1", "الدرس 2", "الدرس 3"]}},
                        {{"module": "اسم الوحدة 3", "objective": "الهدف من الوحدة", "lessons": ["الدرس 1", "الدرس 2", "الدرس 3"]}}
                    ],
                    "offer_engineering": {{
                        "core_price": "السعر الاستراتيجي المقترح مع التبرير النفسي",
                        "bonuses": [
                            {{"name": "اسم مكافأة 1", "value": "قيمتها المادية", "why_it_works": "لماذا ستجبر العميل على الشراء؟"}},
                            {{"name": "اسم مكافأة 2", "value": "قيمتها المادية", "why_it_works": "لماذا ستجبر العميل على الشراء؟"}}
                        ],
                        "risk_reversal": "ضمان استرجاع قوي وغير تقليدي"
                    }},
                    "landing_page_copy": {{
                        "hook_headline": "عنوان رئيسي يخطف الانتباه فوراً",
                        "emotional_story": "فقرة تضرب على وتر المشكلة والألم",
                        "the_solution": "تقديم المنتج كمنقذ وحيد",
                        "call_to_action": "نص الزر (مختلف عن اشترِ الآن)"
                    }}
                }}
                """
                
                try:
                    chat_completion = client.chat.completions.create(
                        messages=[
                            {"role": "system", "content": "أنت أفضل مسوق ومهندس منتجات رقمية في العالم. تخرج البيانات بصيغة JSON فقط."},
                            {"role": "user", "content": prompt}
                        ],
                        model="llama-3.3-70b-versatile",
                        temperature=0.7,
                        max_tokens=6000,
                        response_format={"type": "json_object"}
                    )
                    
                    data = json.loads(chat_completion.choices[0].message.content)
                    
                    # ==========================================
                    # 5. عرض النتائج بالتصميم الفاخر
                    # ==========================================
                    st.balloons()
                    
                    tab1, tab2, tab3, tab4 = st.tabs(["🎯 السوق والتموضع", "📚 هندسة المنهج", "💰 العرض المالي", "🌐 صفحة الهبوط"])
                    
                    with tab1:
                        st.markdown('<div class="metric-card">', unsafe_allow_html=True)
                        st.subheader("📌 التموضع والهوية")
                        st.markdown(f"**🔥 اسم المنتج:** `{data['brand_positioning']['product_name']}`")
                        st.markdown(f"**⚡ الوعد الكبير:** {data['brand_positioning']['grand_promise']}")
                        st.markdown(f"**⚙️ الآلية الفريدة:** {data['brand_positioning']['unique_mechanism']}")
                        st.markdown('</div>', unsafe_allow_html=True)
                        
                        st.markdown('<div class="metric-card">', unsafe_allow_html=True)
                        st.subheader("🕵️ أبحاث السوق")
                        st.write(f"**العميل المثالي:** {data['market_research']['avatar']}")
                        st.write(f"**الرغبة النهائية:** {data['market_research']['ultimate_desire']}")
                        st.write("**أعمق آلام العميل:**")
                        for pain in data['market_research']['deep_pains']:
                            st.markdown(f"- 🩸 {pain}")
                        st.markdown('</div>', unsafe_allow_html=True)
                        
                    with tab2:
                        st.subheader("🎓 هيكل الأكاديمية / الكورس")
                        for i, mod in enumerate(data['course_curriculum']):
                            with st.expander(f"📦 الوحدة {i+1}: {mod['module']}", expanded=(i==0)):
                                st.info(f"**الهدف:** {mod['objective']}")
                                for lesson in mod['lessons']:
                                    st.markdown(f"▶️ {lesson}")
                                    
                    with tab3:
                        st.markdown('<div class="metric-card">', unsafe_allow_html=True)
                        st.subheader("💎 استراتيجية التسعير")
                        st.success(f"**السعر الموصى به:** {data['offer_engineering']['core_price']}")
                        st.warning(f"**🛡️ ضمان البيع:** {data['offer_engineering']['risk_reversal']}")
                        st.markdown('</div>', unsafe_allow_html=True)
                        
                        st.subheader("🎁 المكافآت (Bonuses)")
                        for bonus in data['offer_engineering']['bonuses']:
                            st.markdown(f"""
                            * **{bonus['name']}** (القيمة: {bonus['value']})
                            * *لماذا وضعناها؟* {bonus['why_it_works']}
                            """)
                            
                    with tab4:
                        st.subheader("نص صفحة الهبوط (Copywriting)")
                        st.markdown(f"# {data['landing_page_copy']['hook_headline']}")
                        st.markdown("---")
                        st.markdown(f"*{data['landing_page_copy']['emotional_story']}*")
                        st.markdown("---")
                        st.success(f"**الحل:** {data['landing_page_copy']['the_solution']}")
                        st.button(data['landing_page_copy']['call_to_action'], type="primary", use_container_width=True)

                except Exception as e:
                    st.error(f"حدث خطأ أثناء الهندسة العكسية. تأكد من أن مهارتك واضحة. التفاصيل التقنية: {e}")
        else:
            st.warning("أدخل تفاصيل مهاراتك أولاً لنتمكن من بناء الإمبراطورية.")
else:
    st.info("👈 يرجى إدخال مفتاح Groq API في القائمة الجانبية للبدء.")
