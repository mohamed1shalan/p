# Cross-Validation and Metrics Functions using sklearn

from sklearn.model_selection import (
    LeaveOneGroupOut, LeavePGroupsOut, ShuffleSplit, StratifiedShuffleSplit,
    GroupShuffleSplit, RepeatedKFold, RepeatedStratifiedKFold
)
from sklearn.metrics import (
    accuracy_score, precision_score, recall_score, f1_score, fbeta_score,
    classification_report, confusion_matrix, roc_auc_score, roc_curve,
    precision_recall_curve, average_precision_score, log_loss, hinge_loss
)
import numpy as np

#######################################
# Cross-Validation Methods
#######################################

# LeaveOneGroupOut splits the dataset so that each group is left out once as test set.
def leave_one_group_out(X, y, groups):
    logo = LeaveOneGroupOut()
    return list(logo.split(X, y, groups))


# LeavePGroupsOut leaves P groups out for each split.
def leave_p_groups_out(X, y, groups, p=2):
    lpgo = LeavePGroupsOut(n_groups=p)
    return list(lpgo.split(X, y, groups))


# ShuffleSplit generates random train/test splits.
def shuffle_split(X, y, test_size=0.25, n_splits=5):
    ss = ShuffleSplit(n_splits=n_splits, test_size=test_size)
    return list(ss.split(X, y))


# StratifiedShuffleSplit preserves class distribution when shuffling.
def stratified_shuffle_split(X, y, test_size=0.25, n_splits=5):
    sss = StratifiedShuffleSplit(n_splits=n_splits, test_size=test_size)
    return list(sss.split(X, y))


# GroupShuffleSplit keeps groups together while shuffling.
def group_shuffle_split(X, y, groups, test_size=0.25, n_splits=5):
    gss = GroupShuffleSplit(n_splits=n_splits, test_size=test_size)
    return list(gss.split(X, y, groups))


# RepeatedKFold repeats K-Fold cross-validation multiple times with different splits.
def repeated_kfold(X, y, n_splits=5, n_repeats=2):
    rkf = RepeatedKFold(n_splits=n_splits, n_repeats=n_repeats)
    return list(rkf.split(X, y))


# RepeatedStratifiedKFold repeats Stratified K-Fold preserving class balance.
def repeated_stratified_kfold(X, y, n_splits=5, n_repeats=2):
    rskf = RepeatedStratifiedKFold(n_splits=n_splits, n_repeats=n_repeats)
    return list(rskf.split(X, y))


#######################################
# Metrics Methods
#######################################

# accuracy_score measures the proportion of correctly classified samples.
def get_accuracy(y_true, y_pred):
    return accuracy_score(y_true, y_pred)


# precision_score measures the proportion of positive predictions that are correct.
from typing import Literal

def get_precision(
    y_true,
    y_pred,
    average: Literal['micro', 'macro', 'samples', 'weighted', 'binary'] = 'binary'
):
    return precision_score(y_true, y_pred, average=average)


# recall_score measures the proportion of actual positives that are correctly identified.
def get_recall(
    y_true,
    y_pred,
    average: 'Literal["micro", "macro", "samples", "weighted", "binary"]' = 'binary'
):
    return recall_score(y_true, y_pred, average=average)


# f1_score is the harmonic mean of precision and recall.
def get_f1(
    y_true,
    y_pred,
    average: 'Literal["micro", "macro", "samples", "weighted", "binary"]' = 'binary'
):
    return f1_score(y_true, y_pred, average=average)


# fbeta_score allows adjusting the balance between precision and recall using beta.
def get_fbeta(
    y_true,
    y_pred,
    beta=2,
    average: 'Literal["micro", "macro", "samples", "weighted", "binary"]' = 'binary'
):
    return fbeta_score(y_true, y_pred, beta=beta, average=average)


# classification_report gives a summary of precision, recall, f1-score, and support.
def get_classification_report(y_true, y_pred):
    return classification_report(y_true, y_pred)


# confusion_matrix shows the counts of true vs predicted classifications.
def get_confusion_matrix(y_true, y_pred):
    return confusion_matrix(y_true, y_pred)


# roc_auc_score computes the Area Under the ROC Curve.
def get_roc_auc(y_true, y_scores):
    return roc_auc_score(y_true, y_scores)


# roc_curve provides the false positive rate, true positive rate, and thresholds.
def get_roc_curve(y_true, y_scores):
    return roc_curve(y_true, y_scores)


# precision_recall_curve gives precision-recall pairs for different thresholds.
def get_precision_recall_curve(y_true, y_scores):
    return precision_recall_curve(y_true, y_scores)


# average_precision_score summarizes the precision-recall curve into a single value.
def get_average_precision(y_true, y_scores):
    return average_precision_score(y_true, y_scores)


# log_loss measures the performance of a classifier by penalizing false predictions.
def get_log_loss(y_true, y_prob):
    return log_loss(y_true, y_prob)


# hinge_loss is used for "maximum-margin" classification like SVMs.
def get_hinge_loss(y_true, pred_decision):
    return hinge_loss(y_true, pred_decision)