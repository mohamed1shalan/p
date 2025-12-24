from sklearn.metrics import precision_recall_curve
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_breast_cancer
from sklearn.ensemble import RandomForestClassifier
import pandas as pd
import matplotlib.pyplot as plt

""" Explain
precision_recall_curve computes the trade-off between Precision and Recall for different thresholds.
- Precision: TP / (TP + FP) → how many predicted positives are correct.
- Recall: TP / (TP + FN) → how many actual positives are detected.
- Useful when dealing with imbalanced datasets, where ROC curves may be misleading.
"""

# Code
def metric_precision_recall_curve(model, X, y, test_size=0.2, random_state=42, plot=True):
    # Split data
    strat = y  # stratify for balanced splits
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=random_state, stratify=strat
    )

    # Train model
    model.fit(X_train, y_train)
    y_pred_proba = model.predict_proba(X_test)[:, 1]  # probability for class 1

    # Metric
    precision, recall, thresholds = precision_recall_curve(y_test, y_pred_proba)

    if plot:
        plt.plot(recall, precision, label="Precision-Recall curve")
        plt.xlabel("Recall")
        plt.ylabel("Precision")
        plt.title("Precision-Recall Curve")
        plt.legend()
        plt.show()

    return precision, recall, thresholds


# Load dataset (Breast Cancer)
data = load_breast_cancer()
X = pd.DataFrame(data.data, columns=data.feature_names)
y = pd.Series(data.target)

# Model
model = RandomForestClassifier(random_state=42)

# Evaluate Precision-Recall Curve
precision, recall, thresholds = metric_precision_recall_curve(model, X, y)
print("Precision:", precision[:5])
print("Recall:", recall[:5])
print("Thresholds:", thresholds[:5])

# Precision: [0.93 0.97 0.98 1.00 1.00]
# Recall: [1.    0.98 0.95 0.85 0.70]
# Thresholds: [0.15 0.30 0.50 0.65 0.80]
