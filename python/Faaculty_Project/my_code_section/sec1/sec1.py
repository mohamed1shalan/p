# الفرق بين Pandas و NumPy:

# 📌 NumPy:
# - تُستخدم لإجراء العمليات الرياضية على المصفوفات (Arrays).
# - تعمل بكفاءة عالية على البيانات الرقمية المتجانسة (كل القيم من نفس النوع مثل أرقام فقط).
# - مناسبة للعمليات الحسابية المعقدة والمعالجة الرياضية.
# - مصفوفة متعددة الأبعاد.

# 📌 Pandas:
# - تُستخدم لتحليل ومعالجة البيانات المهيكلة مثل الجداول (CSV, Excel).
# - تدعم أنواع بيانات مختلفة داخل نفس الجدول (أرقام، نصوص، تواريخ...).
# - تعتمد على Series (عمود واحد) و DataFrame (جدول مكوّن من صفوف وأعمدة).
# - أسهل في التعامل مع البيانات الحقيقية بفضل استخدام التسميات (Labels).
# - قوية جدًا في تنظيف البيانات، التعامل مع القيم المفقودة، والفرز، والتصفية.

# ✅ خلاصة:
# - استخدم NumPy عند الحاجة لأداء رياضي عالي وعمليات على مصفوفات رقمية.
# - استخدم Pandas عندما تتعامل مع ملفات بيانات (مثل CSV/Excel) وتحتاج لتحليلها وتنظيمها.

# أمثلة بسيطة:

import numpy as np
import pandas as pd

# مثال باستخدام NumPy
arr = np.array([1, 2, 3, 4])
print("متوسط باستخدام NumPy:", arr.mean())

# مثال باستخدام Pandas
df = pd.DataFrame({'Marks': [1, 2, 3, 4]})
print("متوسط باستخدام Pandas:", df['Marks'].mean())

A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
print(np.dot(A, B))  # Matrix multiplication
print(np.matmul(A, B))  # the same output as dot
x = np.array([1, 2])
y = np.array([3, 4])
print(np.dot(x, y))  # Dot product: 1*3 + 2*4 = 11
print(np.matmul(x, y))  # Error (matmul requires at least

dt = np.dtype([('name', 'U10'), ('age', 'i4'), ('weight', 'f4')])
data = np.array([('Alice', 25, 55.5), ('Bob', 30, 70.2)], dtype=dt)
print(data['name'])  # Output: ['Alice' 'Bob']
print(data['age'])  # Output: [25 30 ]

arr = np.array([1, 2, np.nan, 4, 5])
mean = np.nanmean(arr)  # Ignores NaN
print(mean)  # Output: 3.0

arr = np.array([1, 2, 3, 4])
np.add(arr, 10, out=arr)  # In-place modification
print(arr)  # Output: [11 12 13 14]

A = np.array([[4, -2], [1, 1]])
eigenvalues, eigenvectors = np.linalg.eig(A)
print("Eigenvalues:", eigenvalues)
print("Eigenvectors:\n", eigenvectors)

arr = np.array([1, 2, 2, 3, 3, 3, 4])
unique_values, counts = np.unique(arr, return_counts=True)
print("Unique values:", unique_values)  # كل القيم بدون تكرار
print("Counts:", counts)


# Load dataset (assuming numerical data)
data = np.loadtxt("python\data science\data.csv", delimiter=",",
                  skiprows=1)  # Skip header row
print(data[:5])  # Print first 5 rows
print("Mean:", np.mean(data))
print("Median:", np.median(data))
print("Standard Deviation:", np.std(data))


def min_max_normalize(data):
    return (data - np.min(data)) / (np.max(data) - np.min(data))


normalized_data = min_max_normalize(data)
print(normalized_data)

# يجعل كل القيم بين 0 و 1.
# مفيد جدًا قبل إدخال البيانات في نموذج تعلم آلي (Machine Learning).

# انتجنج ارقام عشوائيه
np.random.seed(42)  # تثبيت العشوائية للحصول على نفس القيم دائمًا
# 10 صفوف × 5 أعمدة size >> عدد القيم
data = np.random.randint(20, 60, size=(10, 5))
print(data)

reshaped_data = data.reshape(5, 2, -1)  # يعيد تشكيلها إلى 5 مجموعات
transposed_data = data.T               # التبديل: الصفوف ⇄ الأعمدة
print(reshaped_data)
