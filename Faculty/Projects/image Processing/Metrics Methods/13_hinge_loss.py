from sklearn.metrics import hinge_loss
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_breast_cancer
from sklearn.svm import LinearSVC
import pandas as pd

""" Explain
hinge_loss is mainly used for "maximum-margin" classification (like SVMs).
- It measures how well the decision boundary separates classes.
- Perfectly classified samples inside the margin are penalized.
- Lower values mean a better model.
- Works only for classifiers that output decision function scores (not probabilities).
"""

# Code
def metric_hinge_loss(model, X, y, test_size=0.2, random_state=42):
    # Split data
    strat = y
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=random_state, stratify=strat
    )

    # Train model
    model.fit(X_train, y_train)
    y_decision = model.decision_function(X_test)  # decision scores

    # Metric
    loss = hinge_loss(y_test, y_decision)
    return loss


# Load dataset (Breast Cancer)
data = load_breast_cancer()
X = pd.DataFrame(data.data, columns=data.feature_names)
y = pd.Series(data.target)

# Model (SVM with linear kernel)
model = LinearSVC(random_state=42, dual=False, max_iter=5000)

# Evaluate Hinge Loss
loss_value = metric_hinge_loss(model, X, y)
print("Hinge Loss:", loss_value)

# Hinge Loss: 0.07
