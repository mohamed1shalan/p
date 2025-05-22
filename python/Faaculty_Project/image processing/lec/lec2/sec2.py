# >>>>>>>>>>>< Load data


# استيراد دالة تحميل بيانات Iris من مكتبة scikit-learn
# المكتبة الرئيسية: sklearn.datasets
# الدالة: load_iris() لتحميل مجموعة بيانات زهور السوسن الشهيرة
from sklearn.impute import SimpleImputer  # << اداه لمعالجه القيم المفقوده
import pandas as pd

import numpy as np
from sklearn.datasets import *

# تحميل البيانات وتعيينها للمتغير iris
# كائن iris يحتوي على:
# - data: الميزات (القياسات)
# - target: التصنيفات (أنواع الزهور)
# - feature_names: أسماء الميزات
# - target_names: أسماء الأصناف
iris = load_iris()

# فصل الميزات عن التصنيفات
# X: مصفوفة تحتوي على قياسات الأزهار (150 عينة × 4 ميزات)
# y: مصفوفة تحتوي على تصنيفات الأزهار (150 تصنيفًا)
X = iris.data  # الميزات (Features)
y = iris.target  # التصنيفات (Labels)

# الحصول على الأسماء الوصفية
feature_names = iris.feature_names  # أسماء الميزات الأربع
target_names = iris.target_names  # أسماء الأصناف الثلاثة

# عرض المعلومات الأساسية عن البيانات
print("أسماء الميزات:", feature_names)  # طباعة أسماء الميزات
print("أسماء الأصناف:", target_names)  # طباعة أسماء أنواع الزهور
# طباعة شكل المصفوفة (عدد العينات والميزات)
print("حجم مجموعة البيانات:", X.shape)

# ملاحظات إضافية:
# 1. البيانات تحتوي على:
#    - 150 عينة (50 من كل صنف)
#    - 4 ميزات لكل عينة:
#      * طول السبل (sepal length)
#      * عرض السبل (sepal width)
#      * طول البتلة (petal length)
#      * عرض البتلة (petal width)
#
# 2. التصنيفات تمثل 3 أنواع من زهور السوسن:
#    - setosa
#    - versicolor
#    - virginica
#
# 3. هذا الكود يعتبر نقطة بداية لأي مشروع تعلم آلي باستخدام هذه البيانات
#
# 4. للتحقق من تثبيت المكتبة بشكل صحيح، يمكنك تنفيذ:
#    import sklearn
#    print(sklearn.__version__)
#    (يجب أن يكون الإصدار 0.24 أو أحدث)

# مثال إضافي: عرض أول 5 عينات من البيانات
print("\nأول 5 عينات من البيانات:")
print(X[:5])

# مثال إضافي: عرض توزيع التصنيفات
print("\nتوزيع التصنيفات لكل نوع:", np.bincount(y))
# الناتج المتوقع: [50 50 50] (50 عينة لكل صنف)


# preprocessing >>>
# Handle missing values.
# Encode categorical variables.
# Scale features.
# Select/extract features.


X = np.array([[1, 2], [np.nan, 3], [7, 6]])
# << استخدم المتوسط لملء القيم المفقودة
imputer = SimpleImputer(strategy='mean')
X_imputed = imputer.fit_transform(X)
# X_imputed البياات الجديده مع القي مالمستبدله
# .........
# from sklearn.preprocessing import OneHotEncoder

# X = [['red'], ['blue'], ['green'], ['blue']]
# encoder = OneHotEncoder(sparse_output=False)
# X_encoded = encoder.fit_transform(X)

# print("Original data:\n", X)
# print("Encoded data:\n", X_encoded)
# الغرض: تحويل البيانات الفئوية (النصية) إلى تنسيق رقمي يفهمه نموذج التعلم الآلي
# sparse_output=False: يعيد مصفوفة عادية بدلًا من مصفوفة sparse

# Original data:
#  [['red'], ['blue'], ['green'], ['blue']]

# Encoded data:
#  [[0. 0. 1.]  # red
#  [1. 0. 0.]  # blue
#  [0. 1. 0.]  # green
#  [1. 0. 0.]] # blue
# ظظ............
# from sklearn.preprocessing import StandardScaler

# X = [[1, 2], [3, 4], [5, 6]]
# scaler = StandardScaler()
# X_scaled = scaler.fit_transform(X)

# print("Original data:\n", X)
# print("Scaled data:\n", X_scaled)


# Original data:
#  [[1, 2], [3, 4], [5, 6]]

# Scaled data:
#  [[-1.22474487 -1.22474487]
#  [ 0.          0.        ]
#  [ 1.22474487  1.22474487]]
# .............
# from sklearn.preprocessing import MinMaxScaler

# X = [[1, 2], [3, 4], [5, 6]]
# scaler = MinMaxScaler()
# X_normalized = scaler.fit_transform(X)

# print("Original data:\n", X)
# print("Normalized data:\n", X_normalized)

# Original data:
#  [[1, 2], [3, 4], [5, 6]]

# Normalized data:
#  [[0.  0. ]
#  [0.5 0.5]
#  [1.  1. ]]
