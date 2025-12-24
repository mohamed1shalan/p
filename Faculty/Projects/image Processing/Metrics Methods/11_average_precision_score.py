from sklearn.metrics import average_precision_score
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_breast_cancer
from sklearn.ensemble import RandomForestClassifier
import pandas as pd

""" Explain
average_precision_score summarizes the precision-recall curve into a single number.
- It is the weighted mean of precisions at each threshold, with the increase in recall as the weight.
- A high score indicates both high precision and high recall.
- Especially useful for imbalanced datasets.
"""

# Code
def metric_average_precision_score(model, X, y, test_size=0.2, random_state=42):
    # Split data
    strat = y
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=random_state, stratify=strat
    )

    # Train model
    model.fit(X_train, y_train)
    y_pred_proba = model.predict_proba(X_test)[:, 1]

    # Metric
    avg_precision = average_precision_score(y_test, y_pred_proba)
    return avg_precision


# Load dataset (Breast Cancer)
data = load_breast_cancer()
X = pd.DataFrame(data.data, columns=data.feature_names)
y = pd.Series(data.target)

# Model
model = RandomForestClassifier(random_state=42)

# Evaluate Average Precision Score
avg_precision = metric_average_precision_score(model, X, y)
print("Average Precision Score:", avg_precision)

# Average Precision Score: 0.9938
