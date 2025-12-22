# Core Libraries
import numpy as np

# Classification Models
from sklearn.linear_model import LogisticRegression, SGDClassifier, RidgeClassifier, RidgeClassifierCV, PassiveAggressiveClassifier, Perceptron
from sklearn.svm import LinearSVC, SVC, NuSVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import (
    RandomForestClassifier, ExtraTreesClassifier, GradientBoostingClassifier,
    AdaBoostClassifier, BaggingClassifier, VotingClassifier, StackingClassifier
)
from sklearn.neighbors import KNeighborsClassifier, RadiusNeighborsClassifier
from sklearn.naive_bayes import (
    GaussianNB, MultinomialNB, BernoulliNB, ComplementNB, CategoricalNB
)
from sklearn.neural_network import MLPClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis, QuadraticDiscriminantAnalysis

# Regression Models
from sklearn.linear_model import (
    LinearRegression, Ridge, RidgeCV, Lasso, LassoCV, ElasticNet, ElasticNetCV,
    LassoLars, LassoLarsCV, Lars, LarsCV, OrthogonalMatchingPursuit,
    OrthogonalMatchingPursuitCV, BayesianRidge, ARDRegression, SGDRegressor,
    PassiveAggressiveRegressor, RANSACRegressor, TheilSenRegressor, HuberRegressor
)
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import (
    RandomForestRegressor, ExtraTreesRegressor, GradientBoostingRegressor,
    AdaBoostRegressor, BaggingRegressor, VotingRegressor, StackingRegressor
)
from sklearn.neighbors import KNeighborsRegressor, RadiusNeighborsRegressor
from sklearn.neural_network import MLPRegressor
from sklearn.svm import SVR, NuSVR, LinearSVR
from sklearn.kernel_ridge import KernelRidge
from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.isotonic import IsotonicRegression

# Clustering Models
from sklearn.cluster import (
    KMeans, MiniBatchKMeans, AffinityPropagation, MeanShift,
    SpectralClustering, AgglomerativeClustering, DBSCAN, OPTICS, Birch,
    FeatureAgglomeration, SpectralBiclustering, SpectralCoclustering
)

# Dimensionality Reduction
from sklearn.decomposition import (
    PCA, IncrementalPCA, KernelPCA, SparsePCA, MiniBatchSparsePCA,
    TruncatedSVD, FastICA, FactorAnalysis, NMF, LatentDirichletAllocation,
    DictionaryLearning, MiniBatchDictionaryLearning, SparseCoder
)
from sklearn.manifold import TSNE, Isomap, LocallyLinearEmbedding, SpectralEmbedding, MDS

# Preprocessing
from sklearn.preprocessing import (
    StandardScaler, MinMaxScaler, MaxAbsScaler, RobustScaler, Normalizer,
    QuantileTransformer, PowerTransformer, LabelEncoder, LabelBinarizer,
    MultiLabelBinarizer, OneHotEncoder, OrdinalEncoder, Binarizer,
    FunctionTransformer, PolynomialFeatures, SplineTransformer, KBinsDiscretizer
)

# Feature Selection
from sklearn.feature_selection import (
    SelectKBest, SelectPercentile, SelectFpr, SelectFdr, SelectFwe,
    GenericUnivariateSelect, VarianceThreshold, SelectFromModel, RFE, f_classif
)

# Model Selection & CV
from sklearn.model_selection import (
    train_test_split, cross_val_score, cross_validate, validation_curve,
    learning_curve, GridSearchCV, RandomizedSearchCV, ParameterGrid, ParameterSampler, KFold,
    StratifiedKFold, GroupKFold, StratifiedGroupKFold, TimeSeriesSplit,
    LeaveOneOut, LeavePOut, LeaveOneGroupOut, LeavePGroupsOut,
    ShuffleSplit, StratifiedShuffleSplit, GroupShuffleSplit,
    RepeatedKFold, RepeatedStratifiedKFold
)

# Metrics
from sklearn.metrics import (
    accuracy_score, precision_score, recall_score, f1_score, fbeta_score,
    classification_report, confusion_matrix, roc_auc_score, roc_curve,
    precision_recall_curve, average_precision_score, log_loss, hinge_loss,
    jaccard_score, matthews_corrcoef, cohen_kappa_score, hamming_loss,
    zero_one_loss, mean_squared_error, mean_absolute_error,
    mean_absolute_percentage_error, median_absolute_error, max_error,
    r2_score, explained_variance_score, mean_squared_log_error,
    mean_poisson_deviance, mean_gamma_deviance, adjusted_rand_score,
    adjusted_mutual_info_score, normalized_mutual_info_score,
    rand_score, mutual_info_score, homogeneity_score, completeness_score,
    v_measure_score, fowlkes_mallows_score, silhouette_score,
    calinski_harabasz_score, davies_bouldin_score
)

# Datasets
from sklearn.datasets import make_classification, make_regression, make_blobs
from sklearn.datasets import load_iris, load_wine, load_breast_cancer, load_diabetes


# Logistic Regression: Train a logistic regression model and predict the test set
def logistic_regression(X_train, y_train, X_test):
    model = LogisticRegression(max_iter=1000)
    model.fit(X_train, y_train)
    return model.predict(X_test)

# Linear SVC: Train a linear Support Vector Classifier and predict the test set
def linear_svc(X_train, y_train, X_test):
    model = LinearSVC(max_iter=2000)
    model.fit(X_train, y_train)
    return model.predict(X_test)

# Support Vector Classifier: Train a non-linear SVC and predict the test set
def svc_classifier(X_train, y_train, X_test):
    model = SVC()
    model.fit(X_train, y_train)
    return model.predict(X_test)

# NuSVC: Train a NuSVC model and predict the test set
def nu_svc_classifier(X_train, y_train, X_test):
    model = NuSVC()
    model.fit(X_train, y_train)
    return model.predict(X_test)

# Decision Tree: Train a decision tree classifier and predict the test set
def decision_tree(X_train, y_train, X_test):
    model = DecisionTreeClassifier()
    model.fit(X_train, y_train)
    return model.predict(X_test)

# Random Forest: Train a random forest classifier and predict the test set
def random_forest(X_train, y_train, X_test):
    model = RandomForestClassifier()
    model.fit(X_train, y_train)
    return model.predict(X_test)

# Extra Trees: Train an extra trees classifier and predict the test set
def extra_trees(X_train, y_train, X_test):
    model = ExtraTreesClassifier()
    model.fit(X_train, y_train)
    return model.predict(X_test)

# Gradient Boosting: Train a gradient boosting classifier and predict the test set
def gradient_boosting(X_train, y_train, X_test):
    model = GradientBoostingClassifier()
    model.fit(X_train, y_train)
    return model.predict(X_test)

# AdaBoost: Train an AdaBoost classifier and predict the test set
def ada_boost(X_train, y_train, X_test):
    model = AdaBoostClassifier()
    model.fit(X_train, y_train)
    return model.predict(X_test)

# Bagging: Train a bagging classifier and predict the test set
def bagging_classifier(X_train, y_train, X_test):
    model = BaggingClassifier()
    model.fit(X_train, y_train)
    return model.predict(X_test)

# Voting Classifier (Soft Voting): Combine models using soft voting for prediction
def voting_classifier(X_train, y_train, X_test):
    model1 = LogisticRegression(max_iter=1000)
    model2 = DecisionTreeClassifier()
    model3 = KNeighborsClassifier()
    model = VotingClassifier(estimators=[('lr', model1), ('dt', model2), ('knn', model3)], voting='soft')
    model.fit(X_train, y_train)
    return model.predict(X_test)

# Stacking Classifier: Use stacking to combine multiple classifiers for prediction
def stacking_classifier(X_train, y_train, X_test):
    estimators = [('rf', RandomForestClassifier()), ('svc', SVC(probability=True))]
    model = StackingClassifier(estimators=estimators, final_estimator=LogisticRegression())
    model.fit(X_train, y_train)
    return model.predict(X_test)

# K-Nearest Neighbors: Train a K-Nearest Neighbors classifier and predict the test set
def knn_classifier(X_train, y_train, X_test):
    model = KNeighborsClassifier()
    model.fit(X_train, y_train)
    return model.predict(X_test)

# Radius Neighbors: Train a Radius Neighbors classifier and predict the test set
def radius_neighbors_classifier(X_train, y_train, X_test):
    model = RadiusNeighborsClassifier()
    model.fit(X_train, y_train)
    return model.predict(X_test)

# Gaussian Naive Bayes: Train a Gaussian Naive Bayes classifier and predict the test set
def gaussian_nb(X_train, y_train, X_test):
    model = GaussianNB()
    model.fit(X_train, y_train)
    return model.predict(X_test)

# Multinomial Naive Bayes: Train a Multinomial Naive Bayes classifier and predict the test set
def multinomial_nb(X_train, y_train, X_test):
    model = MultinomialNB()
    model.fit(X_train, y_train)
    return model.predict(X_test)

# Bernoulli Naive Bayes: Train a Bernoulli Naive Bayes classifier and predict the test set
def bernoulli_nb(X_train, y_train, X_test):
    model = BernoulliNB()
    model.fit(X_train, y_train)
    return model.predict(X_test)

# Complement Naive Bayes: Train a Complement Naive Bayes classifier and predict the test set
def complement_nb(X_train, y_train, X_test):
    model = ComplementNB()
    model.fit(X_train, y_train)
    return model.predict(X_test)

# Categorical Naive Bayes: Train a Categorical Naive Bayes classifier and predict the test set
def categorical_nb(X_train, y_train, X_test):
    model = CategoricalNB()
    model.fit(X_train, y_train)
    return model.predict(X_test)

# Multi-Layer Perceptron: Train a multi-layer perceptron and predict the test set
def mlp_classifier(X_train, y_train, X_test):
    model = MLPClassifier(max_iter=1000)
    model.fit(X_train, y_train)
    return model.predict(X_test)




from sklearn.linear_model import (
    SGDClassifier, RidgeClassifier, RidgeClassifierCV,
    PassiveAggressiveClassifier, Perceptron,
    LinearRegression, Ridge, RidgeCV, Lasso, LassoCV,
    ElasticNet, ElasticNetCV, LassoLars, LassoLarsCV,
    Lars, LarsCV, OrthogonalMatchingPursuit, OrthogonalMatchingPursuitCV
)
from sklearn.discriminant_analysis import (
    QuadraticDiscriminantAnalysis, LinearDiscriminantAnalysis
)

# ---------------------- Classification Models ----------------------

def sgd_classifier():
    """
    Stochastic Gradient Descent Classifier
    بيعمل تدريب باستخدام الـ Gradient Descent بس على بيانات صغيرة عشوائية (mini-batches)
    بيكون سريع ومناسب للداتا الكبيرة جداً.
    """
    return SGDClassifier()

def ridge_classifier():
    """
    Ridge Classifier
    زي الـ Ridge Regression لكن للـ classification.
    بيضيف regularization (L2 penalty) عشان يمنع overfitting.
    """
    return RidgeClassifier()

def ridge_classifier_cv():
    """
    Ridge Classifier مع Cross Validation
    بيختار أفضل قيمة للـ regularization parameter (alpha) تلقائياً باستخدام cross validation.
    """
    return RidgeClassifierCV()

def passive_aggressive_classifier():
    """
    Passive Aggressive Classifier
    بيعمل update للوزن بس لما النموذج يغلط (aggressive)،
    ولو صح ما بيغيرش حاجة (passive).
    مناسب للـ Online Learning.
    """
    return PassiveAggressiveClassifier()

def perceptron_classifier():
    """
    Perceptron
    أبسط neural network (خلي بالك مش deep).
    بيحاول يفصل الـ data بخط مستقيم (linear decision boundary).
    """
    return Perceptron()

def lda_classifier():
    """
    Linear Discriminant Analysis (LDA)
    بيفترض ان الداتا بتتبع توزيع طبيعي (Gaussian) بنفس الـ covariance.
    بيعمل خط فاصل خطي linear boundary.
    """
    return LinearDiscriminantAnalysis()

def qda_classifier():
    """
    Quadratic Discriminant Analysis (QDA)
    زي LDA بس بيسمح لكل class يكون له covariance مختلف.
    بيعمل decision boundaries منحنية (quadratic).
    """
    return QuadraticDiscriminantAnalysis()


# ---------------------- Regression Models ----------------------

def linear_regression():
    """
    Linear Regression
    أبسط نموذج انحدار خطي، بيدور على خط أو مستوى بيقلل مجموع الأخطاء (Least Squares).
    """
    return LinearRegression()

def ridge_regression():
    """
    Ridge Regression
    زي الـ Linear Regression بس بيضيف Regularization L2
    عشان يقلل overfitting.
    """
    return Ridge()

def ridge_regression_cv():
    """
    Ridge Regression مع Cross Validation
    بيعمل tuning لقيمة الـ alpha (الـ regularization parameter) أوتوماتيك.
    """
    return RidgeCV()

def lasso_regression():
    """
    Lasso Regression
    Linear Regression مع Regularization L1
    بيصفر coefficients مش مهمة -> بيساعد في feature selection.
    """
    return Lasso()

def lasso_regression_cv():
    """
    Lasso Regression مع Cross Validation
    بيختار alpha المناسب أوتوماتيك باستخدام cross validation.
    """
    return LassoCV()

def elastic_net():
    """
    Elastic Net
    مزيج من L1 (lasso) + L2 (ridge).
    بيجمع بين feature selection + تقليل overfitting.
    """
    return ElasticNet()

def elastic_net_cv():
    """
    Elastic Net مع Cross Validation
    بيختار أفضل قيم للـ alpha والـ l1_ratio أوتوماتيك.
    """
    return ElasticNetCV()

def lasso_lars():
    """
    LassoLars (Least Angle Regression)
    نسخة أسرع من Lasso لو عدد الـ features كبير.
    """
    return LassoLars()

def lasso_lars_cv():
    """
    LassoLars مع Cross Validation
    بيحدد أفضل alpha أوتوماتيك.
    """
    return LassoLarsCV()

def lars_regression():
    """
    Lars (Least Angle Regression)
    شبيه بالـ Forward Stepwise Selection بس أسرع.
    """
    return Lars()

def lars_cv():
    """
    Lars مع Cross Validation
    بيختار أفضل عدد من الـ steps أوتوماتيك.
    """
    return LarsCV()

def omp_regression():
    """
    Orthogonal Matching Pursuit (OMP)
    خوارزمية greedy لاختيار features مهمة واحدة ورا التانية.
    بتستخدم في الـ sparse regression.
    """
    return OrthogonalMatchingPursuit()

def omp_regression_cv():
    """
    OMP مع Cross Validation
    بيختار تلقائياً عدد الـ features اللي يستخدمها.
    """
    return OrthogonalMatchingPursuitCV()


# 1. Bayesian Ridge Regression
def bayesian_ridge_regressor():
    # يستخدم بايز لتقدير المعاملات مع وجود احتماليات (probabilistic approach)
    return BayesianRidge()


# 2. ARD Regression
def ard_regression():
    # يحدد المتغيرات المهمة (feature selection) تلقائيًا عبر توزيعات بايزية
    return ARDRegression()


# 3. Stochastic Gradient Descent Regressor
def sgd_regressor():
    # يعتمد على الانحدار التدريجي العشوائي (سريع ومناسب للبيانات الكبيرة)
    return SGDRegressor()


# 4. Passive Aggressive Regressor
def passive_aggressive_regressor():
    # يتعلم بسرعة ولا يحدث تغييرات كبيرة إلا عند وجود خطأ
    return PassiveAggressiveRegressor()


# 5. RANSAC Regressor
def ransac_regressor():
    # يتجاهل القيم الشاذة (outliers) ويبحث عن أفضل subset للبيانات
    return RANSACRegressor()


# 6. Theil-Sen Regressor
def theil_sen_regressor():
    # مقاوم للقيم الشاذة ويعتمد على median بدلاً من mean
    return TheilSenRegressor()


# 7. Huber Regressor
def huber_regressor():
    # خليط بين MSE و MAE، قوي ضد القيم الشاذة
    return HuberRegressor()


# 8. Decision Tree Regressor
def decision_tree_regressor():
    # يعتمد على تقسيم البيانات لعقد (Nodes) لفهم الأنماط
    return DecisionTreeRegressor()


# 9. Random Forest Regressor
def random_forest_regressor():
    # مجموعة أشجار قرار (ensemble) لتحسين الدقة
    return RandomForestRegressor()


# 10. Extra Trees Regressor
def extra_trees_regressor():
    # مشابه للـ Random Forest لكن يستخدم تقسيمات عشوائية أكثر
    return ExtraTreesRegressor()


# 11. Gradient Boosting Regressor
def gradient_boosting_regressor():
    # يبني عدة نماذج بشكل متسلسل لتصحيح أخطاء النماذج السابقة
    return GradientBoostingRegressor()


# 12. AdaBoost Regressor
def adaboost_regressor():
    # يعطي وزن أكبر للأخطاء السابقة ويحاول تحسينها
    return AdaBoostRegressor()


# 13. Bagging Regressor
def bagging_regressor():
    # يأخذ عينات عشوائية (bootstrapping) ويبني عدة نماذج
    return BaggingRegressor()


# 14. Voting Regressor
def voting_regressor(estimators):
    # يجمع عدة موديلات (ensemble) ويأخذ المتوسط للتنبؤ
    return VotingRegressor(estimators=estimators)


# 15. Stacking Regressor
def stacking_regressor(estimators, final_estimator):
    # يجمع عدة موديلات باستخدام موديل نهائي (meta-model)
    return StackingRegressor(estimators=estimators, final_estimator=final_estimator)


# 16. K-Neighbors Regressor
def knn_regressor():
    # يعتمد على أقرب K جيران للتنبؤ بالقيمة
    return KNeighborsRegressor()


# 17. Radius Neighbors Regressor
def radius_neighbors_regressor():
    # يعتمد على النقاط داخل نصف قطر معين بدلاً من عدد محدد من الجيران
    return RadiusNeighborsRegressor()


# 18. Multi-layer Perceptron Regressor
def mlp_regressor():
    # شبكة عصبية (Neural Network) متعددة الطبقات للتنبؤ
    return MLPRegressor()


# 19. Support Vector Regressor (SVR)
def svr_regressor():
    # يعتمد على Support Vector Machine لتقدير خط أفضل ضمن حدود (margin)
    return SVR()


# 20. Nu-Support Vector Regressor (NuSVR)
def nusvr_regressor():
    # نسخة من SVR لكن تتحكم بمعاملات الدعم بعدد مختلف
    return NuSVR()


# ================= Regression Methods =================

# Linear Support Vector Regression: fits a linear SVR model and predicts target values.
def linear_svr(X_train, y_train, X_test):
    model = LinearSVR(max_iter=2000)
    model.fit(X_train, y_train)
    return model.predict(X_test)

# Kernel Ridge Regression: combines ridge regression with the kernel trick for non-linear data.
def kernel_ridge(X_train, y_train, X_test, gamma=0.5):
    model = KernelRidge(gamma=gamma)
    model.fit(X_train, y_train)
    return model.predict(X_test)

# Gaussian Process Regression: probabilistic regression that provides predictions with uncertainty.
def gaussian_process_regressor(X_train, y_train, X_test):
    model = GaussianProcessRegressor()
    model.fit(X_train, y_train)
    return model.predict(X_test)

# Isotonic Regression: fits a monotonic (non-decreasing) regression model.
def isotonic_regression(X_train, y_train, X_test):
    model = IsotonicRegression(out_of_bounds="clip")
    model.fit(X_train.ravel(), y_train)
    return model.predict(X_test.ravel())

# ================= Clustering Methods =================

# KMeans Clustering: partitions data into 'k' clusters by minimizing intra-cluster variance.
def kmeans(X, n_clusters=3):
    model = KMeans(n_clusters=n_clusters, random_state=0)
    model.fit(X)
    return model.predict(X)

# Mini-Batch KMeans: faster version of KMeans using small random batches.
def minibatch_kmeans(X, n_clusters=3):
    model = MiniBatchKMeans(n_clusters=n_clusters, random_state=0, batch_size=20)
    model.fit(X)
    return model.predict(X)

# Affinity Propagation: clustering based on message passing between points; auto-detects number of clusters.
def affinity_propagation(X):
    model = AffinityPropagation(random_state=0)
    model.fit(X)
    return model.predict(X)

# Mean Shift: clusters data by finding areas of high density; number of clusters is determined automatically.
def mean_shift(X):
    model = MeanShift()
    model.fit(X)
    return model.predict(X)

# Spectral Clustering: uses graph theory and eigenvalues to cluster complex-shaped data.
def spectral_clustering(X, n_clusters=3):
    model = SpectralClustering(n_clusters=n_clusters, assign_labels="discretize", random_state=0)
    model.fit(X)
    return model.labels_

# Agglomerative Clustering: hierarchical clustering that merges samples step by step.
def agglomerative_clustering(X, n_clusters=3):
    model = AgglomerativeClustering(n_clusters=n_clusters)
    model.fit(X)
    return model.labels_

# DBSCAN: density-based clustering that can detect noise/outliers.
def dbscan(X, eps=0.5, min_samples=5):
    model = DBSCAN(eps=eps, min_samples=min_samples)
    model.fit(X)
    return model.labels_

# OPTICS: density-based clustering similar to DBSCAN but handles varying densities better.
def optics(X, min_samples=5):
    model = OPTICS(min_samples=min_samples)
    model.fit(X)
    return model.labels_

# Birch: hierarchical clustering method optimized for very large datasets.
def birch(X, n_clusters=3):
    model = Birch(n_clusters=n_clusters)
    model.fit(X)
    return model.labels_

# Feature Agglomeration: clusters features instead of samples to reduce dimensionality.
def feature_agglomeration(X, n_clusters=2):
    model = FeatureAgglomeration(n_clusters=n_clusters)
    model.fit(X)
    return model.labels_

# Spectral Biclustering: simultaneously clusters rows and columns (e.g., gene expression data).
def spectral_biclustering(X, n_clusters=2):
    from sklearn.utils.validation import check_array
    X = check_array(X, ensure_min_features=2)  # fix for biclustering
    model = SpectralBiclustering(n_clusters=n_clusters, random_state=0)
    model.fit(X)
    return model.row_labels_

# Spectral Co-Clustering: co-clusters rows and columns into groups.
def spectral_coclustering(X, n_clusters=2):
    from sklearn.utils.validation import check_array
    X = check_array(X, ensure_min_features=2)
    model = SpectralCoclustering(n_clusters=n_clusters, random_state=0)
    model.fit(X)
    return model.row_labels_

# ================= Dimensionality Reduction =================

# Principal Component Analysis (PCA): reduces dimensionality while preserving maximum variance.
def pca(X, n_components=2):
    model = PCA(n_components=n_components)
    return model.fit_transform(X)

# Incremental PCA: PCA that processes data in batches, useful for large datasets.
def incremental_pca(X, n_components=2):
    model = IncrementalPCA(n_components=n_components, batch_size=10)
    return model.fit_transform(X)

# Kernel PCA: non-linear dimensionality reduction using kernels (e.g., RBF).
def kernel_pca(X, n_components=2, kernel: 'Literal["linear", "poly", "rbf", "sigmoid", "cosine", "precomputed"]' = "rbf"):
    model = KernelPCA(n_components=n_components, kernel=kernel)
    return model.fit_transform(X)

# Sparse PCA: dimensionality reduction producing sparse components (many zeros).
def sparse_pca(X, n_components=2):
    model = SparsePCA(n_components=n_components, random_state=0)
    return model.fit_transform(X)

#######################################
# Dimensionality Reduction Methods
#######################################

# MiniBatchSparsePCA performs Sparse PCA using mini-batch optimization.
def minibatch_sparse_pca(X, n_components=2):
    model = MiniBatchSparsePCA(n_components=n_components)
    return model.fit_transform(X)


# TruncatedSVD performs dimensionality reduction using Singular Value Decomposition.
def truncated_svd(X, n_components=2):
    model = TruncatedSVD(n_components=n_components)
    return model.fit_transform(X)


# FastICA separates mixed signals into independent components.
def fast_ica(X, n_components=2):
    model = FastICA(n_components=n_components)
    return model.fit_transform(X)


# FactorAnalysis models data using latent factors.
def factor_analysis(X, n_components=2):
    model = FactorAnalysis(n_components=n_components)
    return model.fit_transform(X)


# NMF decomposes data into non-negative factors.
def nmf(X, n_components=2):
    model = NMF(n_components=n_components)
    return model.fit_transform(X)


# LatentDirichletAllocation is used for topic modeling.
def lda(X, n_components=2):
    model = LatentDirichletAllocation(n_components=n_components)
    return model.fit_transform(X)


# TSNE maps high-dimensional data to 2D/3D for visualization.
def tsne(X, n_components=2):
    model = TSNE(n_components=n_components)
    return model.fit_transform(X)


# Isomap preserves geodesic distances in a low-dimensional space.
def isomap(X, n_components=2):
    model = Isomap(n_components=n_components)
    return model.fit_transform(X)


# LocallyLinearEmbedding preserves local neighborhood structure in embedding.
def lle(X, n_components=2):
    model = LocallyLinearEmbedding(n_components=n_components)
    return model.fit_transform(X)


# SpectralEmbedding uses graph Laplacian for non-linear dimensionality reduction.
def spectral_embedding(X, n_components=2):
    model = SpectralEmbedding(n_components=n_components)
    return model.fit_transform(X)


# MDS reduces dimensions while preserving pairwise distances.
def mds(X, n_components=2):
    model = MDS(n_components=n_components)
    return model.fit_transform(X)


# DictionaryLearning learns a dictionary of sparse components.
def dictionary_learning(X, n_components=2):
    model = DictionaryLearning(n_components=n_components)
    return model.fit_transform(X)


# MiniBatchDictionaryLearning is a faster version of DictionaryLearning using mini-batches.
def minibatch_dictionary_learning(X, n_components=2):
    model = MiniBatchDictionaryLearning(n_components=n_components)
    return model.fit_transform(X)


# SparseCoder encodes data using a pre-learned dictionary.
def sparse_coder(X, dictionary):
    model = SparseCoder(dictionary=dictionary.components_)
    return model.transform(X)


#######################################
# Preprocessing Methods
#######################################

# StandardScaler standardizes features by removing the mean and scaling to unit variance.
def standard_scaler(X):
    scaler = StandardScaler()
    return scaler.fit_transform(X)


# MinMaxScaler scales features to a given range (default 0 to 1).
def minmax_scaler(X):
    scaler = MinMaxScaler()
    return scaler.fit_transform(X)


# MaxAbsScaler scales features by their maximum absolute value.
def maxabs_scaler(X):
    scaler = MaxAbsScaler()
    return scaler.fit_transform(X)


# RobustScaler scales features using median and interquartile range (robust to outliers).
def robust_scaler(X):
    scaler = RobustScaler()
    return scaler.fit_transform(X)


# Normalizer scales each sample to have unit norm (row-wise).
def normalizer(X):
    scaler = Normalizer()
    return scaler.fit_transform(X)


# QuantileTransformer transforms features to follow a uniform or normal distribution.
def quantile_transformer(X, output_distribution: 'Literal["uniform", "normal"]' = 'uniform'):
    scaler = QuantileTransformer(output_distribution=output_distribution)
    return scaler.fit_transform(X)


# PowerTransformer: Applies a power transformation to make data more Gaussian-like.
def power_transformer(X_train, X_test):
    pt = PowerTransformer()
    X_train_transformed = pt.fit_transform(X_train)
    X_test_transformed = pt.transform(X_test)
    return X_train_transformed, X_test_transformed

# LabelEncoder: Encodes target labels with values between 0 and n_classes-1.
def label_encoder(y_train, y_test):
    le = LabelEncoder()
    y_train_encoded = le.fit_transform(y_train)
    y_test_encoded = le.transform(y_test)
    return y_train_encoded, y_test_encoded

# LabelBinarizer: Binarizes labels in a one-vs-all fashion.
def label_binarizer(y_train, y_test):
    lb = LabelBinarizer()
    y_train_binarized = lb.fit_transform(y_train)
    y_test_binarized = lb.transform(y_test)
    return y_train_binarized, y_test_binarized

# MultiLabelBinarizer: Transforms a list of multi-label tuples into a binary matrix.
def multi_label_binarizer(y_train, y_test):
    mlb = MultiLabelBinarizer()
    y_train_binarized = mlb.fit_transform(y_train)
    y_test_binarized = mlb.transform(y_test)
    return y_train_binarized, y_test_binarized

# OneHotEncoder: Encodes categorical integer features as a one-hot numeric array.
def one_hot_encoder(X_train, X_test):
    ohe = OneHotEncoder(handle_unknown='ignore')
    X_train_encoded = ohe.fit_transform(X_train)
    X_test_encoded = ohe.transform(X_test)
    return X_train_encoded, X_test_encoded

# OrdinalEncoder: Encodes categorical features into an integer array.
def ordinal_encoder(X_train, X_test):
    oe = OrdinalEncoder()
    X_train_encoded = oe.fit_transform(X_train)
    X_test_encoded = oe.transform(X_test)
    return X_train_encoded, X_test_encoded

# Binarizer: Binarizes data based on a threshold, turning feature values into 0 or 1.
def binarizer(X_train, X_test, threshold=0.0):
    binarizer = Binarizer(threshold=threshold)
    X_train_binarized = binarizer.fit_transform(X_train)
    X_test_binarized = binarizer.transform(X_test)
    return X_train_binarized, X_test_binarized

# FunctionTransformer: Constructs a transformer from an arbitrary callable function.
def function_transformer(X_train, X_test):
    # Example function: log transform
    transformer = FunctionTransformer(np.log1p)
    X_train_transformed = transformer.transform(X_train)
    X_test_transformed = transformer.transform(X_test)
    return X_train_transformed, X_test_transformed

# PolynomialFeatures: Generates polynomial and interaction features.
def polynomial_features(X_train, X_test, degree=2):
    poly = PolynomialFeatures(degree=degree)
    X_train_poly = poly.fit_transform(X_train)
    X_test_poly = poly.transform(X_test)
    return X_train_poly, X_test_poly

# SplineTransformer: Generates B-spline basis functions for features.
def spline_transformer(X_train, X_test, n_knots=5):
    spline = SplineTransformer(n_knots=n_knots)
    X_train_spline = spline.fit_transform(X_train)
    X_test_spline = spline.transform(X_test)
    return X_train_spline, X_test_spline

# KBinsDiscretizer: Bins continuous data into intervals.
def kbins_discretizer(X_train, X_test, n_bins=5):
    discretizer = KBinsDiscretizer(n_bins=n_bins, encode='ordinal')
    X_train_discretized = discretizer.fit_transform(X_train)
    X_test_discretized = discretizer.transform(X_test)
    return X_train_discretized, X_test_discretized

### Feature Selection Methods ###

# SelectKBest: Selects features according to the k highest scores.
def select_k_best(X_train, y_train, X_test, k=10):
    selector = SelectKBest(score_func=f_classif, k=k)
    X_train_selected = selector.fit_transform(X_train, y_train)
    X_test_selected = selector.transform(X_test)
    return X_train_selected, X_test_selected

# SelectPercentile: Selects features according to a percentile of the highest scores.
def select_percentile(X_train, y_train, X_test, percentile=10):
    selector = SelectPercentile(score_func=f_classif, percentile=percentile)
    X_train_selected = selector.fit_transform(X_train, y_train)
    X_test_selected = selector.transform(X_test)
    return X_train_selected, X_test_selected

# SelectFpr: Selects features based on a false positive rate test.
def select_fpr(X_train, y_train, X_test, alpha=0.05):
    selector = SelectFpr(score_func=f_classif, alpha=alpha)
    X_train_selected = selector.fit_transform(X_train, y_train)
    X_test_selected = selector.transform(X_test)
    return X_train_selected, X_test_selected

# SelectFdr: Selects features based on an estimated false discovery rate.
def select_fdr(X_train, y_train, X_test, alpha=0.05):
    selector = SelectFdr(score_func=f_classif, alpha=alpha)
    X_train_selected = selector.fit_transform(X_train, y_train)
    X_test_selected = selector.transform(X_test)
    return X_train_selected, X_test_selected

# SelectFwe: Selects features based on the family-wise error rate.
def select_fwe(X_train, y_train, X_test, alpha=0.05):
    selector = SelectFwe(score_func=f_classif, alpha=alpha)
    X_train_selected = selector.fit_transform(X_train, y_train)
    X_test_selected = selector.transform(X_test)
    return X_train_selected, X_test_selected

# GenericUnivariateSelect: Performs univariate feature selection with a configurable strategy.
def generic_univariate_select(X_train, y_train, X_test):
    # mode can be 'percentile', 'k_best', 'fpr', 'fdr', 'fwe'
    selector = GenericUnivariateSelect(score_func=f_classif, mode='k_best', param=10)
    X_train_selected = selector.fit_transform(X_train, y_train)
    X_test_selected = selector.transform(X_test)
    return X_train_selected, X_test_selected

# VarianceThreshold: Removes all features with low-variance.
def variance_threshold(X_train, X_test, threshold=0.0):
    selector = VarianceThreshold(threshold=threshold)
    X_train_selected = selector.fit_transform(X_train)
    X_test_selected = selector.transform(X_test)
    return X_train_selected, X_test_selected

# SelectFromModel: Selects features based on importance weights from a model.
def select_from_model(X_train, y_train, X_test):
    estimator = RandomForestClassifier(n_estimators=50)
    selector = SelectFromModel(estimator=estimator, prefit=False)
    X_train_selected = selector.fit_transform(X_train, y_train)
    X_test_selected = selector.transform(X_test)
    return X_train_selected, X_test_selected

# RFE (Recursive Feature Elimination): Selects features by recursively considering smaller sets of features.
def rfe(X_train, y_train, X_test, n_features_to_select=10):
    estimator = LogisticRegression(max_iter=2000)
    selector = RFE(estimator, n_features_to_select=n_features_to_select, step=1)
    X_train_selected = selector.fit_transform(X_train, y_train)
    X_test_selected = selector.transform(X_test)
    return X_train_selected, X_test_selected


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

# ================== Classification Metrics ==================

def jaccard(y_true, y_pred, average: 'Literal["micro", "macro", "samples", "weighted", "binary"]' = "binary"):
    """تشابه جاكارد: يقيس نسبة التقاطع إلى الاتحاد (0→1)."""
    return jaccard_score(y_true, y_pred, average=average)

def matthews_corr(y_true, y_pred):
    """معامل MCC: يقيس قوة الارتباط ([-1,1])."""
    return matthews_corrcoef(y_true, y_pred)

def cohen_kappa(y_true, y_pred):
    """كابا لـ كوهين: اتفاق معدل بالصدفة ([-1,1])."""
    return cohen_kappa_score(y_true, y_pred)

def hamming(y_true, y_pred):
    """خسارة هامنج: نسبة الملصقات الخاطئة (0→1)."""
    return hamming_loss(y_true, y_pred)

def zero_one(y_true, y_pred):
    """خسارة صفر-واحد: نسبة العينات الخاطئة بالكامل (0→1)."""
    return zero_one_loss(y_true, y_pred)

# ================== Regression Metrics ==================

def mse(y_true, y_pred):
    """MSE: متوسط مربع الخطأ (الأقل أفضل)."""
    return mean_squared_error(y_true, y_pred)

def mae(y_true, y_pred):
    """MAE: متوسط الخطأ المطلق (الأقل أفضل)."""
    return mean_absolute_error(y_true, y_pred)

def mape(y_true, y_pred):
    """MAPE: متوسط نسبة الخطأ (%)."""
    return mean_absolute_percentage_error(y_true, y_pred)

def median_ae(y_true, y_pred):
    """Median AE: الوسيط للأخطاء المطلقة (robust)."""
    return median_absolute_error(y_true, y_pred)

def max_err(y_true, y_pred):
    """أكبر خطأ مطلق (أسوأ حالة)."""
    return max_error(y_true, y_pred)

def r2(y_true, y_pred):
    """R²: نسبة التباين المفسر (<=1، الأعلى أفضل)."""
    return r2_score(y_true, y_pred)

def explained_var(y_true, y_pred):
    """Explained Variance: التباين المفسر (<=1)."""
    return explained_variance_score(y_true, y_pred)

def msle(y_true, y_pred):
    """MSLE: MSE بعد اللوغاريتم (يقبل قيم موجبة فقط)."""
    return mean_squared_log_error(y_true, y_pred)

def poisson_dev(y_true, y_pred):
    """Poisson Deviance: مناسب لبيانات العد (>0)."""
    return mean_poisson_deviance(y_true, y_pred)

def gamma_dev(y_true, y_pred):
    """Gamma Deviance: مناسب لقيم موجبة مستمرة."""
    return mean_gamma_deviance(y_true, y_pred)

# ================== Clustering Metrics ==================

def adjusted_rand(y_true, y_pred):
    """ARI: تشابه عنقدة معدل بالصدفة ([-1,1])."""
    return adjusted_rand_score(y_true, y_pred)

def adjusted_mutual_info(y_true, y_pred):
    """AMI: معلومات مشتركة معدلة (0→1)."""
    return adjusted_mutual_info_score(y_true, y_pred)

def normalized_mutual_info(y_true, y_pred):
    """NMI: معلومات مشتركة مُطبّعة (0→1)."""
    return normalized_mutual_info_score(y_true, y_pred)

def rand(y_true, y_pred):
    """Rand Index: نسبة الاتفاق بدون تعديل (0→1)."""
    return rand_score(y_true, y_pred)

def mutual_info(y_true, y_pred):
    """MI: معلومات مشتركة (>=0، ليس لها حد أعلى)."""
    return mutual_info_score(y_true, y_pred)

# Create toy dataset
X, y = make_blobs(n_samples=100, centers=3, random_state=42)[0:2]
kmeans_model = KMeans(n_clusters=3, random_state=42).fit(X)


# 1. homogeneity_score
# Measures if each cluster contains only members of a single class
print("homogeneity_score:", homogeneity_score(y, kmeans_model.labels_))


# 2. completeness_score
# Measures if all members of a given class are assigned to the same cluster
print("completeness_score:", completeness_score(y, kmeans_model.labels_))


# 3. v_measure_score
# Harmonic mean of homogeneity and completeness
print("v_measure_score:", v_measure_score(y, kmeans_model.labels_))


# 4. fowlkes_mallows_score
# Geometric mean of precision and recall for clustering
print("fowlkes_mallows_score:", fowlkes_mallows_score(y, kmeans_model.labels_))


# 5. silhouette_score
# Measures similarity of points within the same cluster vs other clusters
print("silhouette_score:", silhouette_score(X, kmeans_model.labels_))


# 6. calinski_harabasz_score
# Ratio of between-cluster dispersion and within-cluster dispersion
print("calinski_harabasz_score:", calinski_harabasz_score(X, kmeans_model.labels_))


# 7. davies_bouldin_score
# Average similarity between each cluster and its most similar one (lower is better)
print("davies_bouldin_score:", davies_bouldin_score(X, kmeans_model.labels_))



# ============================
# ⚙️ Pipeline and Compose Methods
# ============================

from sklearn.pipeline import FeatureUnion, make_pipeline, make_union
from sklearn.compose import ColumnTransformer, make_column_transformer, TransformedTargetRegressor
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.linear_model import LinearRegression
import pandas as pd
import numpy as np

# Create toy dataset
df = pd.DataFrame({
    "age": [25, 32, 47, 51],
    "city": ["Cairo", "Giza", "Cairo", "Alex"],
    "income": [3000, 4000, 5000, 6000]
})


# 8. FeatureUnion
# Combine multiple transformers into a single one
fu = FeatureUnion([("scale", StandardScaler())])
print("FeatureUnion created:", fu)


# 9. ColumnTransformer
# Apply different transformations to different columns
ct = ColumnTransformer([
    ("num", StandardScaler(), ["age", "income"]),
    ("cat", OneHotEncoder(), ["city"])
])
print("ColumnTransformer output:\n", ct.fit_transform(df))


# 10. TransformedTargetRegressor
# Applies transformation to target during regression
reg = TransformedTargetRegressor(
    regressor=LinearRegression(),
    transformer=StandardScaler()
)
X_train = df[["age", "income"]]
y_train = df["income"] * 1.5
reg.fit(X_train, y_train)
print("TransformedTargetRegressor prediction:", reg.predict([[30, 3500]]))


# 11. make_pipeline
# Shortcut to build pipeline
pipe = make_pipeline(StandardScaler(), LinearRegression())
pipe.fit(X_train, y_train)
print("make_pipeline prediction:", pipe.predict([[40, 4500]]))


# 12. make_column_transformer
# Shortcut to ColumnTransformer
mct = make_column_transformer(
    (StandardScaler(), ["age", "income"]),
    (OneHotEncoder(), ["city"])
)
print("make_column_transformer output:\n", mct.fit_transform(df))


# 13. make_union
# Shortcut to FeatureUnion
mu = make_union(StandardScaler(), OneHotEncoder(handle_unknown="ignore"))
print("make_union created:", mu)



# ============================
# 🎯 Multiclass and Multilabel Methods
# ============================

from sklearn.multiclass import OneVsRestClassifier, OneVsOneClassifier, OutputCodeClassifier
from sklearn.multioutput import MultiOutputRegressor, MultiOutputClassifier, RegressorChain, ClassifierChain
from sklearn.datasets import make_multilabel_classification
from sklearn.linear_model import LogisticRegression, Ridge
from sklearn.tree import DecisionTreeClassifier

# Create toy datasets
X_ml, Y_ml = make_multilabel_classification(n_samples=100, n_classes=3, random_state=42)[:2]
X_mc, y_mc = make_blobs(n_samples=100, centers=3, random_state=42)[0:2]


# 14. OneVsRestClassifier
# Trains one classifier per class (multilabel/multiclass)
ovr = OneVsRestClassifier(LogisticRegression()).fit(X_ml, Y_ml)
print("OneVsRestClassifier prediction:", ovr.predict(X_ml[:1]))


# 15. OneVsOneClassifier
# Trains one classifier per pair of classes (multiclass only)
ovo = OneVsOneClassifier(LogisticRegression()).fit(X_mc, y_mc)
print("OneVsOneClassifier prediction:", ovo.predict(X_mc[:1]))


# 16. OutputCodeClassifier
# Uses error-correcting codes to handle multiclass problems
ecc = OutputCodeClassifier(LogisticRegression(), code_size=2).fit(X_mc, y_mc)
print("OutputCodeClassifier prediction:", ecc.predict(X_mc[:1]))


# 17. MultiOutputRegressor
# Trains one regressor per target variable
mor = MultiOutputRegressor(Ridge()).fit(X_ml, Y_ml)
print("MultiOutputRegressor prediction:", mor.predict(X_ml[:1]))


# 18. MultiOutputClassifier
# Trains one classifier per target variable
moc = MultiOutputClassifier(DecisionTreeClassifier()).fit(X_ml, Y_ml)
print("MultiOutputClassifier prediction:", moc.predict(X_ml[:1]))


# 19. RegressorChain
# Chains regressors so each model uses predictions of previous as features
rc = RegressorChain(LogisticRegression()).fit(X_ml, Y_ml)
print("RegressorChain prediction:", rc.predict(X_ml[:1]))


# 20. ClassifierChain
# Chains classifiers so each model uses predictions of previous as features
cc = ClassifierChain(LogisticRegression()).fit(X_ml, Y_ml)
print("ClassifierChain prediction:", cc.predict(X_ml[:1]))
