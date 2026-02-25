import streamlit as st
import google.generativeai as genai
import json

# ==========================================
# 1. إعدادات الصفحة والهوية
# ==========================================
st.set_page_config(page_title="SkillForge AI | مصنع المنتجات الرقمية", page_icon="🚀", layout="centered")

st.title("🚀 AI Skill Monetizer (SkillForge)")
st.markdown("### حول أي مهارة إلى نظام دخل متكامل في ثوانٍ.")

# ==========================================
# 2. إعداد مفتاح الـ API (الربط بالذكاء الاصطناعي)
# ==========================================
API_KEY = st.text_input("أدخل مفتاح Google Gemini API الخاص بك (سري):", type="password")

if API_KEY:
    genai.configure(api_key=API_KEY)
    
    # اختيار النموذج اللغوي
    model = genai.GenerativeModel('gemini-1.5-pro')

    # ==========================================
    # 3. واجهة إدخال المهارة
    # ==========================================
    st.markdown("---")
    user_skill = st.text_area(
        "ما هي المهارة أو الخبرة التي تتقنها؟", 
        placeholder="مثال: برمجة إضافات متقدمة لـ Blender باستخدام Python و Geometry Nodes (مثل محركات Ai3DGen أو أدوات الأتمتة)، وأريد تحويل هذه الخبرة إلى منتج رقمي...",
        height=150
    )

    if st.button("🔥 هندسة المنتج الرقمي الآن", use_container_width=True):
        if user_skill:
            with st.spinner("العملاء الأذكياء (Agents) يقومون الآن بهندسة الكورس، قمع المبيعات، وخطة الإطلاق... يرجى الانتظار."):
                
                # ==========================================
                # 4. المحرك الجوهري (The Master Prompt)
                # ==========================================
                prompt = f"""
                أنت نظام AI Skill Monetizer. مهمتك تحويل هذه المهارة إلى منتج رقمي متكامل.
                المهارة: {user_skill}
                
                يجب أن يكون الرد حصرياً بصيغة JSON صحيحة (بدون أي نصوص خارج الـ JSON)، ويحتوي على المفاتيح التالية:
                {{
                    "positioning": {{"promise": "الوعد الرئيسي", "target_audience": "الجمهور المستهدف", "problem": "المشكلة الرئيسية"}},
                    "course_modules": [
                        {{"title": "عنوان الوحدة 1", "lessons": ["درس 1", "درس 2", "درس 3"]}},
                        {{"title": "عنوان الوحدة 2", "lessons": ["درس 1", "درس 2", "درس 3"]}}
                    ],
                    "offer_stack": {{"main_product": "اسم المنتج", "bonus_1": "مكافأة 1", "bonus_2": "مكافأة 2", "price_recommendation": "السعر المقترح بالدولار"}},
                    "landing_page": {{"headline": "عنوان رئيسي جذاب", "subheadline": "عنوان فرعي", "call_to_action": "نص زر الشراء"}}
                }}
                """
                
                try:
                    # إرسال الطلب للذكاء الاصطناعي
                    response = model.generate_content(prompt)
                    
                    # تنظيف الرد لتحويله إلى JSON
                    raw_text = response.text.replace('```json', '').replace('```', '').strip()
                    data = json.loads(raw_text)
                    
                    # ==========================================
                    # 5. عرض النتائج بشكل احترافي
                    # ==========================================
                    st.success("تم بناء نظام الدخل بنجاح! 🎯")
                    
                    tab1, tab2, tab3, tab4 = st.tabs(["📌 التموضع", "🎓 المنهج", "💰 العرض", "🌐 صفحة الهبوط"])
                    
                    with tab1:
                        st.subheader("التموضع الاستراتيجي")
                        st.write(f"**الجمهور المستهدف:** {data['positioning']['target_audience']}")
                        st.write(f"**المشكلة التي نحلها:** {data['positioning']['problem']}")
                        st.info(f"**الوعد الكبير:** {data['positioning']['promise']}")
                        
                    with tab2:
                        st.subheader("هيكل الكورس الجاهز")
                        for i, module in enumerate(data['course_modules']):
                            with st.expander(f"الوحدة {i+1}: {module['title']}"):
                                for lesson in module['lessons']:
                                    st.markdown(f"- {lesson}")
                                    
                    with tab3:
                        st.subheader("هندسة العرض (Offer Stack)")
                        st.write(f"**المنتج الأساسي:** {data['offer_stack']['main_product']}")
                        st.write(f"🎁 **مكافأة 1:** {data['offer_stack']['bonus_1']}")
                        st.write(f"🎁 **مكافأة 2:** {data['offer_stack']['bonus_2']}")
                        st.success(f"**السعر المقترح للإطلاق:** {data['offer_stack']['price_recommendation']}")
                        
                    with tab4:
                        st.subheader("مسودة صفحة الهبوط (Landing Page)")
                        st.markdown(f"## {data['landing_page']['headline']}")
                        st.markdown(f"#### {data['landing_page']['subheadline']}")
                        st.button(data['landing_page']['call_to_action'], type="primary")

                except Exception as e:
                    st.error(f"حدث خطأ أثناء معالجة البيانات. تأكد من جودة الـ API Key أو حاول مرة أخرى. التفاصيل: {e}")
        else:
            st.warning("يرجى إدخال المهارة أولاً.")
else:
    st.info("للبدء، يرجى الحصول على API Key مجاني من Google AI Studio وإدخاله أعلاه.")
