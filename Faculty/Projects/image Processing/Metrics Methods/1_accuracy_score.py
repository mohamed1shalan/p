from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
import pandas as pd

""" Explain
accuracy_score measures the proportion of correct predictions (y_pred == y_true).
It is suitable for balanced classification problems but can be misleading with imbalanced classes.
Formula: Accuracy = (TP + TN) / (TP + TN + FP + FN)
"""

# Code
def metric_accuracy(model, X, y, test_size=0.2, random_state=42, stratify=True):
    # Split (stratify for classification to preserve class ratios)
    strat = y if stratify else None
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=random_state, stratify=strat
    )

    # Fit & predict
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    # Metric
    acc = accuracy_score(y_test, y_pred)
    return acc, y_test, y_pred


# Load data (Iris – balanced multiclass)
data = load_iris()
X = pd.DataFrame(data.data, columns=data.feature_names)
y = pd.Series(data.target)

# Model
model = RandomForestClassifier(random_state=42)

# Evaluate Accuracy
acc, y_test, y_pred = metric_accuracy(model, X, y, test_size=0.2, random_state=42, stratify=True)
print("Accuracy:", acc)


from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
import pandas as pd

""" Explain
accuracy_score measures the proportion of correct predictions (y_pred == y_true).
It is suitable for balanced classification problems but can be misleading with imbalanced classes.
Formula: Accuracy = (TP + TN) / (TP + TN + FP + FN)
"""

# Code
def metric_accuracy(model, X, y, test_size=0.2, random_state=42, stratify=True):
    # Split (stratify for classification to preserve class ratios)
    strat = y if stratify else None
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=random_state, stratify=strat
    )

    # Fit & predict
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    # Metric
    acc = accuracy_score(y_test, y_pred)
    return acc, y_test, y_pred


# Load data (Iris – balanced multiclass)
data = load_iris()
X = pd.DataFrame(data.data, columns=data.feature_names)
y = pd.Series(data.target)

# Model
model = RandomForestClassifier(random_state=42)

# Evaluate Accuracy
acc, y_test, y_pred = metric_accuracy(model, X, y, test_size=0.2, random_state=42, stratify=True)
print("Accuracy:", acc)

# Accuracy: 0.9666666666666667
