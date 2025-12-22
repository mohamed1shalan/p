from sklearn.metrics import recall_score
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_breast_cancer
from sklearn.ensemble import RandomForestClassifier
import pandas as pd

""" Explain
recall_score measures the proportion of actual positives that are correctly identified.
It answers the question: "Of all the true positives, how many did the model detect?"
Formula: Recall = TP / (TP + FN)
Useful when the cost of false negatives is high (e.g., medical diagnosis, fraud detection).
"""

# Code
def metric_recall(model, X, y, test_size=0.2, random_state=42, average="binary"):
    # Split
    strat = y  # keep class balance
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=random_state, stratify=strat
    )

    # Fit & predict
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    # Metric
    rec = recall_score(y_test, y_pred, average=average)
    return rec, y_test, y_pred


# Load data (Breast Cancer – binary classification)
data = load_breast_cancer()
X = pd.DataFrame(data.data, columns=data.feature_names)
y = pd.Series(data.target)

# Model
model = RandomForestClassifier(random_state=42)

# Evaluate Recall
rec, y_test, y_pred = metric_recall(model, X, y, test_size=0.2, random_state=42, average="binary")
print("Recall:", rec)


# Recall: 0.9722222222222222
