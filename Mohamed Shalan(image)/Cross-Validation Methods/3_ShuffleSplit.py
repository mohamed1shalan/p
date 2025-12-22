from sklearn.model_selection import ShuffleSplit
from sklearn.datasets import load_breast_cancer
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import pandas as pd
import numpy as np

""" Explain
ShuffleSplit is a cross-validation strategy that generates train/test indices by randomly
shuffling the dataset and splitting it into training and test sets.
Unlike KFold, the same sample can appear in multiple test sets across different iterations.
It is useful when you want random train/test splits multiple times to evaluate model stability.
"""

# Code
def cross_val_shufflesplit(model, X, y, n_splits=5, test_size=0.2, random_state=42):
    ss = ShuffleSplit(n_splits=n_splits, test_size=test_size, random_state=random_state)
    scores = []

    for train_idx, test_idx in ss.split(X, y):
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

# Model
model = RandomForestClassifier(random_state=42)

# ShuffleSplit CV
scores, mean_score = cross_val_shufflesplit(model, X, y, n_splits=5, test_size=0.2)
print("Scores for each split:", scores)
print("Mean accuracy:", mean_score)


# Scores for each split: [0.956140350877193, 0.9649122807017544, 0.956140350877193, 0.9736842105263158, 0.9473684210526315]
# Mean accuracy: 0.9592491220074174
