import streamlit as st
import pandas as pd
import pickle
import numpy as np
from sklearn.metrics import accuracy_score, precision_score, f1_score, confusion_matrix

model = pickle.load(open('Model.pkl', 'rb'))
cv = pickle.load(open('Victorize.pkl', 'rb'))

with open("test_data.pkl", "rb") as f:
    x_test, y_test = pickle.load(f)

pred = model.predict(x_test)

accuracy = accuracy_score(y_test, pred)
precision = precision_score(y_test, pred)
f1 = f1_score(y_test, pred)
conf_matrix = confusion_matrix(y_test, pred)

st.title("Neural Network Spam Classifier")
st.markdown("اكتب رسالة وسيتم تصنيفها ما إذا كانت Spam أو Ham")

user_input = st.text_input("ادخل الرسالة:")
if user_input:
    vect_msg = cv.transform([user_input]).toarray()
    prediction = model.predict(vect_msg)[0]
    result = "Ham" if prediction == 1 else "Spam"
    st.success(f"النتيجة: {result}")

st.markdown("### معلومات عن نموذج الشبكة العصبية")

info = {
    "نوع الشبكة العصبية": ["Multilayer Perceptron (MLPClassifier)"],
    "عدد الطبقات (Layers)": ["3"],
    "عدد النيورونات في كل طبقة": ["100, 50, 25"],
    "هل الشبكة Fully Connected؟": ["YES"],
    "حجم بيانات الاختبار": [str(x_test.shape[0])],
    "عدد الخصائص (Features)": [str(x_test.shape[1])],
    "الخوارزمية المستخدمة": ["Adam Optimizer"],
    "دالة التفعيل (Activation)": ["ReLU"],
    "أقصى عدد تكرارات للتدريب": ["300"],
    "الدقة (Accuracy)": [f"{100*accuracy:.2f}"],
    "الدقة النوعية (Precision)": [f"{100*precision:.2f}"],
    "F1 Score": [f"{100*f1:.2f}"]
}

info_df = pd.DataFrame(info).T
info_df.columns = ["القيمة"]
info_df.index.name = "الميزة"
st.dataframe(info_df)

st.markdown("### مصفوفة الارتباك")
st.text(conf_matrix)