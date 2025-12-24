from sklearn.metrics import fbeta_score
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_breast_cancer
from sklearn.ensemble import RandomForestClassifier
import pandas as pd

""" Explain
fbeta_score is a generalized version of F1-score.
It allows adjusting the balance between precision and recall using the parameter β (beta).
- If β > 1 → recall is given more weight.
- If β < 1 → precision is given more weight.
Formula: Fβ = (1 + β²) * (Precision * Recall) / (β² * Precision + Recall)
"""

# Code
def metric_fbeta(model, X, y, beta=0.5, test_size=0.2, random_state=42, average="binary"):
    # Split
    strat = y  # preserve class balance
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=random_state, stratify=strat
    )

    # Fit & predict
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    # Metric
    fbeta = fbeta_score(y_test, y_pred, beta=beta, average=average)
    return fbeta, y_test, y_pred


# Load data (Breast Cancer – binary classification)
data = load_breast_cancer()
X = pd.DataFrame(data.data, columns=data.feature_names)
y = pd.Series(data.target)

# Model
model = RandomForestClassifier(random_state=42)

# Evaluate F-beta score
fbeta, y_test, y_pred = metric_fbeta(model, X, y, beta=0.5, test_size=0.2, random_state=42, average="binary")
print("F0.5-score:", fbeta)

# F0.5-score: 0.9811320754716981
