from sklearn.model_selection import RepeatedStratifiedKFold
from sklearn.datasets import load_breast_cancer
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import pandas as pd
import numpy as np

""" Explain
RepeatedStratifiedKFold is a cross-validation strategy that repeats Stratified K-Fold multiple times
with different randomization in each repetition.
It preserves the class distribution (stratification) in each train/test split.
This is especially useful for classification tasks with imbalanced datasets.
"""

# Code
def cross_val_repeated_stratkfold(model, X, y, n_splits=5, n_repeats=3, random_state=42):
    rskf = RepeatedStratifiedKFold(n_splits=n_splits, n_repeats=n_repeats, random_state=random_state)
    scores = []

    for train_idx, test_idx in rskf.split(X, y):
        X_train, X_test = X.iloc[train_idx], X.iloc[test_idx]
        y_train, y_test = y.iloc[train_idx], y.iloc[test_idx]

        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)
        scores.append(accuracy_score(y_test, y_pred))

    return scores, np.mean(scores)


# Load imbalanced dataset (Breast Cancer)
data = load_breast_cancer()
X = pd.DataFrame(data.data, columns=data.feature_names)
y = pd.Series(data.target)

# Model
model = RandomForestClassifier(random_state=42)

# RepeatedStratifiedKFold CV
scores, mean_score = cross_val_repeated_stratkfold(model, X, y, n_splits=5, n_repeats=3)
print("Scores for first 10 splits:", scores[:10], "...")
print("Mean accuracy:", mean_score)


# Scores for first 10 splits: [0.9473684210526315, 0.956140350877193, 0.9385964912280702, 
# 0.9473684210526315, 0.956140350877193, 0.9473684210526315, 
# 0.9385964912280702, 0.956140350877193, 0.9385964912280702, 
# 0.9473684210526315] ...
# Mean accuracy: 0.9479338842975207
