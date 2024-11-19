import numpy as np
import pandas as pd
from sklearn.model_selection import KFold
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics
import os

# Read the merged data and selected features
code_dir = os.path.dirname(os.path.abspath(__file__))
data_file = os.path.join(code_dir, 'refs', 'filtered_data.csv')

filtered_data = pd.read_csv(data_file)

# The last column is the label and the other columns are features.
X = filtered_data.iloc[:, :-1].values  # Extract features
Y = filtered_data.iloc[:, -1].values  # Extract Tags

# Make sure the labels are binary (1 for malignant, 0 for benign)
Y = np.where(Y == 1, 1, 0)  

# Set the number of KFold folds
folds = 5
kf = KFold(n_splits=folds, shuffle=True, random_state=42)

# Storing model evaluation results
svm_scores = []
knn_scores = []

# KFold Cross Validation
for fold, (train_index, test_index) in enumerate(kf.split(X), 1):
    print(f"  Processing Fold {fold}...")

    X_train, X_test = X[train_index], X[test_index]
    y_train, y_test = Y[train_index], Y[test_index]
    
    # SVM Model
    print(f"    Training SVM model for Fold {fold}...")
    svm_model = SVC(probability=True, class_weight='balanced')
    svm_model.fit(X_train, y_train)
    svm_pred = svm_model.predict(X_test)
    
    # KNN Model
    print(f"    Training KNN model for Fold {fold}...")
    knn_model = KNeighborsClassifier(n_neighbors=5)
    knn_model.fit(X_train, y_train)
    knn_pred = knn_model.predict(X_test)
    
    # Calculate the accuracy of SVM and KNN models
    svm_accuracy = metrics.accuracy_score(y_test, svm_pred)
    knn_accuracy = metrics.accuracy_score(y_test, knn_pred)
    
    svm_scores.append(svm_accuracy)
    knn_scores.append(knn_accuracy)

    print(f"    Fold {fold} - SVM Accuracy: {svm_accuracy:.4f}")
    print(f"    Fold {fold} - KNN Accuracy: {knn_accuracy:.4f}")


print("-----SVM Performance (KFold)-----")
print(f"SVM Accuracies for each fold: {svm_scores}")
print(f"Average SVM Accuracy: {np.mean(svm_scores)}")

print("-----KNN Performance (KFold)-----")
print(f"KNN Accuracies for each fold: {knn_scores}")
print(f"Average KNN Accuracy: {np.mean(knn_scores)}")

# Finally, compare the performance of SVM and KNN
if np.mean(svm_scores) > np.mean(knn_scores):
    print("\nSVM is the better model based on KFold cross-validation.")
else:
    print("\nKNN is the better model based on KFold cross-validation.")
