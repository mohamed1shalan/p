from sklearn.model_selection import GroupShuffleSplit
from sklearn.datasets import load_breast_cancer
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import pandas as pd
import numpy as np

""" Explain
GroupShuffleSplit is a cross-validation strategy that randomly splits data into train/test sets
while making sure that the same group is not represented in both training and testing sets.
This is useful when you have grouped data (e.g., patients, sessions, subjects) and want to
avoid data leakage between training and testing.
"""

# Code
def cross_val_groupshufflesplit(model, X, y, groups, n_splits=5, test_size=0.2, random_state=42):
    gss = GroupShuffleSplit(n_splits=n_splits, test_size=test_size, random_state=random_state)
    scores = []

    for train_idx, test_idx in gss.split(X, y, groups):
        # Handle DataFrame/Series
        X_train, X_test = X.iloc[train_idx], X.iloc[test_idx]
        y_train, y_test = y.iloc[train_idx], y.iloc[test_idx]

        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)
        scores.append(accuracy_score(y_test, y_pred))

    return scores, np.mean(scores)


# Load data
data = load_breast_cancer()
X = pd.DataFrame(data.data, columns=data.feature_names)
y = pd.Series(data.target)

# Artificial groups (e.g., patients/sessions)
groups = np.arange(len(y)) % 10   # 10 groups

# Model
model = RandomForestClassifier(random_state=42)

# GroupShuffleSplit CV
scores, mean_score = cross_val_groupshufflesplit(model, X, y, groups, n_splits=5, test_size=0.2)
print("Scores for each split:", scores)
print("Mean accuracy:", mean_score)

# Scores for each split: [0.9473684210526315, 0.956140350877193, 0.9385964912280702, 0.9473684210526315, 0.956140350877193]
# Mean accuracy: 0.9493220068176391
