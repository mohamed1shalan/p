from sklearn.model_selection import StratifiedShuffleSplit
from sklearn.datasets import load_breast_cancer
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import pandas as pd

""" Explain
StratifiedShuffleSplit is a cross-validation strategy that generates random train/test splits
while preserving the percentage of samples for each class.
It is especially useful when dealing with imbalanced datasets, ensuring that both training
and test sets have the same class distribution as the full dataset.
"""

# Code
def cross_val_stratified_shufflesplit(model, X, y, n_splits=5, test_size=0.2, random_state=42):
    sss = StratifiedShuffleSplit(n_splits=n_splits, test_size=test_size, random_state=random_state)
    scores = []

    for train_idx, test_idx in sss.split(X, y):
        X_train, X_test = X.iloc[train_idx], X.iloc[test_idx]
        y_train, y_test = y.iloc[train_idx], y.iloc[test_idx]

        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)
        scores.append(accuracy_score(y_test, y_pred))

    return scores, sum(scores)/len(scores)


# Load imbalanced dataset (Breast Cancer is slightly imbalanced)
data = load_breast_cancer()
X = pd.DataFrame(data.data, columns=data.feature_names)
y = pd.Series(data.target)

# Model
model = RandomForestClassifier(random_state=42)

# StratifiedShuffleSplit CV
scores, mean_score = cross_val_stratified_shufflesplit(model, X, y, n_splits=5, test_size=0.2)
print("Scores for each split:", scores)
print("Mean accuracy:", mean_score)


# Scores for each split: [0.956140350877193, 0.956140350877193, 0.9473684210526315, 0.956140350877193, 0.9473684210526315]
# Mean accuracy: 0.9522315795289684
