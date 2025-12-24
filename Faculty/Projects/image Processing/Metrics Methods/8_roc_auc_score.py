from sklearn.metrics import roc_auc_score
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_breast_cancer
from sklearn.ensemble import RandomForestClassifier
import pandas as pd

""" Explain
roc_auc_score computes the Area Under the Receiver Operating Characteristic Curve (ROC AUC).
- It measures the ability of the classifier to distinguish between classes.
- AUC = 1 means perfect classifier, AUC = 0.5 means random guessing.
- It is commonly used for binary classification with probabilities.
"""

# Code
def metric_roc_auc_score(model, X, y, test_size=0.2, random_state=42):
    # Split data
    strat = y  # stratify for balanced splits
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=random_state, stratify=strat
    )

    # Train model
    model.fit(X_train, y_train)
    y_pred_proba = model.predict_proba(X_test)[:, 1]  # probability for class 1

    # Metric
    auc = roc_auc_score(y_test, y_pred_proba)
    return auc, y_test, y_pred_proba


# Load dataset (Breast Cancer)
data = load_breast_cancer()
X = pd.DataFrame(data.data, columns=data.feature_names)
y = pd.Series(data.target)

# Model
model = RandomForestClassifier(random_state=42)

# Evaluate ROC AUC Score
auc, y_test, y_pred_proba = metric_roc_auc_score(model, X, y)
print("ROC AUC Score:", auc)

# ROC AUC Score: 0.9975
