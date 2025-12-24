from sklearn.metrics import roc_curve
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_breast_cancer
from sklearn.ensemble import RandomForestClassifier
import pandas as pd
import matplotlib.pyplot as plt

""" Explain
roc_curve computes the Receiver Operating Characteristic curve.
- It shows the trade-off between True Positive Rate (TPR = Recall) and False Positive Rate (FPR).
- Useful for evaluating classifier thresholds.
- Often visualized as a curve, with the ROC AUC summarizing performance.
"""

# Code
def metric_roc_curve(model, X, y, test_size=0.2, random_state=42, plot=True):
    # Split data
    strat = y  # stratify for balanced splits
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=random_state, stratify=strat
    )

    # Train model
    model.fit(X_train, y_train)
    y_pred_proba = model.predict_proba(X_test)[:, 1]  # probability for class 1

    # Metric
    fpr, tpr, thresholds = roc_curve(y_test, y_pred_proba)

    if plot:
        plt.plot(fpr, tpr, label="ROC curve")
        plt.plot([0, 1], [0, 1], linestyle="--", color="gray", label="Random")
        plt.xlabel("False Positive Rate")
        plt.ylabel("True Positive Rate (Recall)")
        plt.title("ROC Curve")
        plt.legend()
        plt.show()

    return fpr, tpr, thresholds


# Load dataset (Breast Cancer)
data = load_breast_cancer()
X = pd.DataFrame(data.data, columns=data.feature_names)
y = pd.Series(data.target)

# Model
model = RandomForestClassifier(random_state=42)

# Evaluate ROC Curve
fpr, tpr, thresholds = metric_roc_curve(model, X, y)
print("FPR:", fpr[:5])
print("TPR:", tpr[:5])
print("Thresholds:", thresholds[:5])

# FPR: [0.   0.   0.02 0.02 0.04]
# TPR: [0.   0.98 0.98 1.   1.  ]
# Thresholds: [inf 0.99 0.85 0.75 0.60]
