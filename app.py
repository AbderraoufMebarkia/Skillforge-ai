import streamlit as st
from groq import Groq
import json

# ==========================================
# 1. إعدادات الصفحة والهوية
# ==========================================
st.set_page_config(page_title="SkillForge AI | مصنع المنتجات الرقمية", page_icon="🚀", layout="centered")

st.title("🚀 AI Skill Monetizer (SkillForge)")
st.markdown("### حول أي مهارة إلى نظام دخل متكامل في ثوانٍ.")

# ==========================================
# 2. إعداد مفتاح الـ API (محرك Groq السريع)
# ==========================================
API_KEY = st.text_input("أدخل مفتاح Groq API الخاص بك (سري):", type="password")

if API_KEY:
    # تهيئة عميل Groq
    client = Groq(api_key=API_KEY)

    # ==========================================
    # 3. واجهة إدخال المهارة
    # ==========================================
    st.markdown("---")
    user_skill = st.text_area(
        "ما هي المهارة أو الخبرة التي تتقنها؟", 
        placeholder="مثال: مبرمج إضافات 3D لبلندر، وأريد تحويل خبرتي في برمجة أدوات مثل Ai3DGen إلى كورس ومنتج رقمي مربح...",
        height=150
    )

    if st.button("🔥 هندسة المنتج الرقمي الآن", use_container_width=True):
        if user_skill:
            with st.spinner("🚀 يتم الآن توليد الكورس وقمع المبيعات بسرعة البرق عبر محرك Groq..."):
                
                # ==========================================
                # 4. المحرك الجوهري
                # ==========================================
                prompt = f"""
                أنت خبير هندسة منتجات رقمية وتسويق. قم بتحويل هذه المهارة إلى منتج رقمي متكامل.
                المهارة: {user_skill}
                
                يجب أن ترد حصرياً بصيغة JSON صحيحة، وتحتوي على المفاتيح التالية:
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
                    # إرسال الطلب لـ Groq باستخدام نموذج LLaMA 3
                    chat_completion = client.chat.completions.create(
                        messages=[
                            {
                                "role": "system",
                                "content": "أنت مبرمج وتخرج البيانات بصيغة JSON فقط."
                            },
                            {
                                "role": "user",
                                "content": prompt
                            }
                        ],
                        model="llama3-70b-8192",
                        temperature=0.7,
                        response_format={"type": "json_object"}
                    )
                    
                    # استخراج وتصنيف الرد
                    raw_text = chat_completion.choices[0].message.content
                    data = json.loads(raw_text)
                    
                    # ==========================================
                    # 5. عرض النتائج
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
                    st.error(f"حدث خطأ: {e}")
        else:
            st.warning("يرجى إدخال المهارة أولاً.")
else:
    st.info("للبدء، يرجى الحصول على API Key من منصة Groq وإدخاله أعلاه.")
