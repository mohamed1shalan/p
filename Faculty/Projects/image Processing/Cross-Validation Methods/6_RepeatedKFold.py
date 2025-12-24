from sklearn.model_selection import RepeatedKFold
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import pandas as pd
import numpy as np

""" Explain
RepeatedKFold is a cross-validation strategy that repeats K-Fold cross validation
multiple times with different randomization in each repetition.
It provides a more robust estimate of model performance compared to a single K-Fold run.
Useful when dataset is small and we want to reduce variance in performance estimation.
"""

# Code
def cross_val_repeatedkfold(model, X, y, n_splits=5, n_repeats=3, random_state=42):
    rkf = RepeatedKFold(n_splits=n_splits, n_repeats=n_repeats, random_state=random_state)
    scores = []

    for train_idx, test_idx in rkf.split(X, y):
        X_train, X_test = X.iloc[train_idx], X.iloc[test_idx]
        y_train, y_test = y.iloc[train_idx], y.iloc[test_idx]

        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)
        scores.append(accuracy_score(y_test, y_pred))

    return scores, np.mean(scores)


# Load dataset (Iris for simplicity)
data = load_iris()
X = pd.DataFrame(data.data, columns=data.feature_names)
y = pd.Series(data.target)

# Model
model = RandomForestClassifier(random_state=42)

# RepeatedKFold CV
scores, mean_score = cross_val_repeatedkfold(model, X, y, n_splits=5, n_repeats=3)
print("Scores for each split:", scores[:10], "...")  # عرض أول 10 فقط للاختصار
print("Mean accuracy:", mean_score)


# Scores for each split: [0.9666666666666667, 0.9333333333333333, 0.9666666666666667, 0.9666666666666667, 0.9333333333333333, 0.9666666666666667, 0.9666666666666667, 0.9666666666666667, 0.9333333333333333, 0.9666666666666667] ...
# Mean accuracy: 0.9577777777777778
