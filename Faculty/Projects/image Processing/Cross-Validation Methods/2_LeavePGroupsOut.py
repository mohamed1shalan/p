from sklearn.model_selection import LeavePGroupsOut
from sklearn.datasets import load_breast_cancer
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import pandas as pd
import numpy as np

""" Explain
LeavePGroupsOut (LPGO) is a cross-validation strategy where P groups are left out in each split
as the test set, and the remaining groups are used as the training set.
It is an extension of LeaveOneGroupOut, but instead of leaving one group at a time,
you leave P groups out together.
This is useful when you want to evaluate model performance on multiple groups simultaneously.
"""

# Code
def cross_val_lpgo(model, X, y, groups, p=2):
    lpgo = LeavePGroupsOut(n_groups=p)
    scores = []

    for train_idx, test_idx in lpgo.split(X, y, groups):
        # Handle DataFrame/Series or numpy
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

# LeavePGroupsOut CV
scores, mean_score = cross_val_lpgo(model, X, y, groups, p=2)
print("Scores for each split:", scores)
print("Mean accuracy:", mean_score)

# Scores for each split: [0.9298245614035088, 0.9298245614035088, 0.9210526315789473, 0.9385964912280702, 0.9385964912280702, 0.9210526315789473, 0.9385964912280702, 0.9298245614035088, 0.9210526315789473, 0.9385964912280702]
# Mean accuracy: 0.9305202993652742
