from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_breast_cancer
from sklearn.ensemble import RandomForestClassifier
import pandas as pd

""" Explain
classification_report provides a detailed summary of classification metrics:
- Precision
- Recall
- F1-score
- Support (number of true instances for each class)

It is useful for evaluating multi-class and binary classifiers at once.
"""

# Code
def metric_classification_report(model, X, y, test_size=0.2, random_state=42, target_names=None):
    # Split
    strat = y  # preserve class balance
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=random_state, stratify=strat
    )

    # Fit & predict
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    # Metric
    report = classification_report(y_test, y_pred, target_names=target_names)
    return report, y_test, y_pred


# Load data (Breast Cancer – binary classification)
data = load_breast_cancer()
X = pd.DataFrame(data.data, columns=data.feature_names)
y = pd.Series(data.target)

# Model
model = RandomForestClassifier(random_state=42)

# Evaluate Classification Report
report, y_test, y_pred = metric_classification_report(
    model, X, y, test_size=0.2, random_state=42, target_names=data.target_names
)
print("Classification Report:\n", report)

# Classification Report:
#               precision    recall  f1-score   support

#    malignant       0.95      0.97      0.96        43
#       benign       0.99      0.98      0.99        71

#     accuracy                           0.98       114
#    macro avg       0.97      0.97      0.97       114
# weighted avg       0.98      0.98      0.98       114
