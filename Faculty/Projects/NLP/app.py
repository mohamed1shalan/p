import streamlit as st
import numpy as np
import tensorflow as tf
from tensorflow.keras.datasets import imdb
from tensorflow.keras.preprocessing import sequence # type: ignore

# 1. إعدادات ثابتة (نفس اللي استخدمتها في التدريب)
MAXLEN = 200  # أقصى طول للجملة
MAX_FEATURES = 10000 # عدد الكلمات

@st.cache_resource
def load_model():
    model = tf.keras.models.load_model('my_sentiment_model.keras')
    return model

model = load_model()

word_index = imdb.get_word_index()

def preprocess_text(text):
    words = text.lower().split()
    
    encoded_review = []
    for word in words:
        if word in word_index and word_index[word] + 3 < MAX_FEATURES:
            encoded_review.append(word_index[word] + 3)
        else:
            encoded_review.append(2)
            
    padded_review = sequence.pad_sequences([encoded_review], maxlen=MAXLEN)
    return padded_review

st.set_page_config(page_title="محلل أفلام IMDB", page_icon="🎬")

st.title("🎬 محلل آراء الأفلام (LSTM Model)")
st.write("الموديل ده مدرب على بيانات IMDB باستخدام شبكات عصبية (LSTM).")

st.divider()

# مكان الكتابة
user_input = st.text_area("اكتب رأيك في الفيلم (بالإنجليزي):", height=150, placeholder="Example: This movie was fantastic and the acting was great...")

if st.button("تحليل الرأي"):
    if not user_input.strip():
        st.warning("⚠️ من فضلك اكتب جملة مفيدة.")
    else:
        with st.spinner('جاري التحليل...'):
            try:
                # 1. تجهيز النص
                processed_input = preprocess_text(user_input)
                
                # 2. التوقع
                prediction = model.predict(processed_input)[0][0]
                
                # 3. عرض النتيجة
                st.write("---")
                
                # النتيجة بتطلع رقم من 0 لـ 1 (لأننا مستخدمين Sigmoid)
                # لو قريب من 1 يبقى إيجابي، لو قريب من 0 يبقى سلبي
                
                col1, col2 = st.columns(2)
                
                with col1:
                    st.metric("درجة الإيجابية", f"{prediction:.2%}")
                
                with col2:
                    if prediction > 0.5:
                        st.success("النتيجة: **Review إيجابي (Positive)** 👍")
                        st.balloons()
                    else:
                        st.error("النتيجة: **Review سلبي (Negative)** 👎")
                
                # عرض شريط التقدم
                st.progress(float(prediction))
                
            except Exception as e:
                st.error(f"حصل خطأ: {e}")

st.divider()

# cd python\Faaculty_Project\NLP
# py -m streamlit run app.py