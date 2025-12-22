import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

data = load_iris()
X = data.data            # Features
y = data.target          # Labels
class_names = data.target_names

# تقسيم البيانات
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

# إنشاء الموديل
model = RandomForestClassifier(n_estimators=100, random_state=42)

# التدريب
model.fit(X_train, y_train)

# التوقع
y_pred = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))

plt.figure(figsize=(6,5))
cm = confusion_matrix(y_test, y_pred)
sns.heatmap(cm, annot=True, fmt="d", cmap="Greens",
            xticklabels=class_names, yticklabels=class_names)
plt.title(" Random Forest Confusion Matrix")
plt.xlabel("Predicted Label")
plt.ylabel("True Label")
plt.show()

importances = model.feature_importances_
indices = np.argsort(importances)

plt.figure(figsize=(7,4))
plt.barh(range(len(indices)), importances[indices], align='center', color='forestgreen')
plt.yticks(range(len(indices)), np.array(data.feature_names)[indices])
plt.title(" Feature Importance in Random Forest")
plt.xlabel("Importance Score")
plt.ylabel("Feature")
plt.show()