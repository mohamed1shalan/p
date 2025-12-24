from sklearn.metrics import f1_score
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_breast_cancer
from sklearn.ensemble import RandomForestClassifier
import pandas as pd

""" Explain
f1_score is the harmonic mean of precision and recall.
It balances both metrics, making it useful when classes are imbalanced.
Formula: F1 = 2 * (Precision * Recall) / (Precision + Recall)
It is high only when both precision and recall are high.
"""

# Code
def metric_f1(model, X, y, test_size=0.2, random_state=42, average="binary"):
    # Split
    strat = y  # preserve class balance
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=random_state, stratify=strat
    )

    # Fit & predict
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    # Metric
    f1 = f1_score(y_test, y_pred, average=average)
    return f1, y_test, y_pred


# Load data (Breast Cancer – binary classification)
data = load_breast_cancer()
X = pd.DataFrame(data.data, columns=data.feature_names)
y = pd.Series(data.target)

# Model
model = RandomForestClassifier(random_state=42)

# Evaluate F1-score
f1, y_test, y_pred = metric_f1(model, X, y, test_size=0.2, random_state=42, average="binary")
print("F1-score:", f1)

# F1-score: 0.9769230769230769
