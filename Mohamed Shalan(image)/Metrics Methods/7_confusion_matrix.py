from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_breast_cancer
from sklearn.ensemble import RandomForestClassifier
import pandas as pd

""" Explain
confusion_matrix is a table used to evaluate the performance of a classification model.
It shows:
- True Positives (TP)
- True Negatives (TN)
- False Positives (FP)
- False Negatives (FN)

This helps in understanding how many predictions were correct or incorrect for each class.
"""

# Code
def metric_confusion_matrix(model, X, y, test_size=0.2, random_state=42):
    # Split data
    strat = y  # preserve class balance
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=random_state, stratify=strat
    )

    # Train model
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    # Metric
    cm = confusion_matrix(y_test, y_pred)
    return cm, y_test, y_pred


# Load dataset (Breast Cancer)
data = load_breast_cancer()
X = pd.DataFrame(data.data, columns=data.feature_names)
y = pd.Series(data.target)

# Model
model = RandomForestClassifier(random_state=42)

# Evaluate Confusion Matrix
cm, y_test, y_pred = metric_confusion_matrix(model, X, y)
print("Confusion Matrix:\n", cm)

# Confusion Matrix:
# [[42  1]
#  [ 2 69]]
