from sklearn.model_selection import LeaveOneGroupOut
from sklearn.datasets import load_breast_cancer
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import pandas as pd
import numpy as np

""" Explain
LeaveOneGroupOut (LOGO) is a cross-validation strategy where each group is left out once
as the test set, and the rest of the groups are used as the training set.
It is especially useful when you have data divided into distinct groups (e.g., patients, sessions, subjects).
Each group is completely excluded from training when used as test data, which prevents data leakage
between training and test sets.
"""

# Code
def cross_val_logo(model, X, y, groups):
    logo = LeaveOneGroupOut()
    scores = []

    for train_idx, test_idx in logo.split(X, y, groups):
        # لو X و y DataFrame/Series
        if isinstance(X, pd.DataFrame):
            X_train, X_test = X.iloc[train_idx], X.iloc[test_idx]
        else:
            X_train, X_test = X[train_idx], X[test_idx]

        if isinstance(y, (pd.Series, pd.DataFrame)):
            y_train, y_test = y.iloc[train_idx], y.iloc[test_idx]
        else:
            y_train, y_test = y[train_idx], y[test_idx]

        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)
        scores.append(accuracy_score(y_test, y_pred))

    return scores, np.mean(scores)


# Load data
data = load_breast_cancer()
X = pd.DataFrame(data.data, columns=data.feature_names)
y = pd.Series(data.target)

# Create artificial groups (e.g., based on modulo of sample index)
groups = np.arange(len(y)) % 5  # 5 groups

# Model
model = RandomForestClassifier(random_state=42)

# LeaveOneGroupOut CV
scores, mean_score = cross_val_logo(model, X, y, groups)
print("Scores for each group:", scores)
print("Mean accuracy:", mean_score)


# Scores for each group: [0.9298245614035088, 0.9210526315789473, 0.9385964912280702, 0.9210526315789473, 0.9385964912280702]
# Mean accuracy: 0.9290245612272946
