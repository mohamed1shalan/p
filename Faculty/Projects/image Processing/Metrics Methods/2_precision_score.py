from sklearn.metrics import precision_score
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_breast_cancer
from sklearn.ensemble import RandomForestClassifier
import pandas as pd

""" Explain
precision_score measures the proportion of positive predictions that are actually correct.
It answers the question: "Of all the samples predicted as positive, how many are truly positive?"
Formula: Precision = TP / (TP + FP)
Useful when the cost of false positives is high (e.g., spam detection).
"""

# Code
def metric_precision(model, X, y, test_size=0.2, random_state=42, average="binary"):
    # Split
    strat = y  # preserve class balance
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=random_state, stratify=strat
    )

    # Fit & predict
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    # Metric
    prec = precision_score(y_test, y_pred, average=average)
    return prec, y_test, y_pred


# Load data (Breast Cancer – binary classification)
data = load_breast_cancer()
X = pd.DataFrame(data.data, columns=data.feature_names)
y = pd.Series(data.target)

# Model
model = RandomForestClassifier(random_state=42)

# Evaluate Precision
prec, y_test, y_pred = metric_precision(model, X, y, test_size=0.2, random_state=42, average="binary")
print("Precision:", prec)

# Precision: 0.9818181818181818
