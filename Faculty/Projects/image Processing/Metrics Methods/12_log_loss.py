from sklearn.metrics import log_loss
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_breast_cancer
from sklearn.ensemble import RandomForestClassifier
import pandas as pd

""" Explain
log_loss (Logarithmic Loss or Cross-Entropy Loss) measures the performance of a classification model 
that outputs probabilities instead of class labels.

- Lower values are better.
- It heavily penalizes confident wrong predictions.
- Used a lot in probabilistic models (e.g., logistic regression, neural networks).
"""

# Code
def metric_log_loss(model, X, y, test_size=0.2, random_state=42):
    # Split data
    strat = y
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=random_state, stratify=strat
    )

    # Train model
    model.fit(X_train, y_train)
    y_pred_proba = model.predict_proba(X_test)

    # Metric
    loss = log_loss(y_test, y_pred_proba)
    return loss


# Load dataset (Breast Cancer)
data = load_breast_cancer()
X = pd.DataFrame(data.data, columns=data.feature_names)
y = pd.Series(data.target)

# Model
model = RandomForestClassifier(random_state=42)

# Evaluate Log Loss
loss_value = metric_log_loss(model, X, y)
print("Log Loss:", loss_value)


# Log Loss: 0.1752
