import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn import metrics
from joblib import dump  # 用于保存模型
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

# Data partitioning
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.3, random_state=42)
print("Distribution of target variables in training set:")
print(pd.Series(y_train).value_counts())
print("Test set target variable distribution:")
print(pd.Series(y_test).value_counts())


# Using RBF kernel function to train SVM model
svm_rbf_model = SVC(kernel='rbf', probability=True, class_weight='balanced')
svm_rbf_model.fit(X_train, y_train)

# Make predictions on the test set
y_pred_test = svm_rbf_model.predict(X_test)

# Print Classification Report
print("Test Classification Report:")
print(metrics.classification_report(y_test, y_pred_test, target_names=['Benign', 'Malignant']))

# Calculate accuracy
accuracy = metrics.accuracy_score(y_test, y_pred_test)
print(f"Test Accuracy: {accuracy}")

# Save the trained model
dump(svm_rbf_model, 'svm_rbf_model.joblib')
print("The model has been saved as 'svm_rbf_model.joblib'")

# ------------------------------
# Save the features and target data of the test set to a CSV file

# Extract the name of the feature column
feature_columns = filtered_data.columns[:-1]

# Save the features of the test set (X_test) to a CSV file, removing the target column
test_features = pd.DataFrame(X_test, columns=feature_columns)
test_features.to_csv(os.path.join(code_dir,'refs', 'X_test.csv'), index=False)
print("The test set features have been saved as 'X_test.csv'。")

# Save the target column of the test set (y_test) to a CSV file
test_target = pd.DataFrame(y_test, columns=['Malignancy'])
test_target.to_csv(os.path.join(code_dir,'refs', 'y_test.csv'), index=False)
print("The test set target column is saved as 'y_test.csv'。")
