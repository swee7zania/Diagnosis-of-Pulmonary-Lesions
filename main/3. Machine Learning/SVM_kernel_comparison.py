import numpy as np
import pandas as pd
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
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

# Randomly split the training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.3, random_state=42)

# Choose different kernel functions for comparison
kernels = ['poly', 'rbf', 'sigmoid']

# Store the evaluation results of each kernel function
kernel_scores = {}

# Traversing different kernel functions
for kernel in kernels:
    print(f"Testing kernel function: {kernel}")
    svm_model = SVC(kernel=kernel, probability=True, class_weight='balanced')
    svm_model.fit(X_train, y_train)
    
    # Making predictions
    y_pred_test = svm_model.predict(X_test)
    
    # Calculate and output classification report
    accuracy = metrics.accuracy_score(y_test, y_pred_test)
    print(f"{kernel.capitalize()} Kernel Classification Report:")
    print(metrics.classification_report(y_test, y_pred_test, target_names=['Benign', 'Malignant']))
    
    # Store the accuracy of each kernel function
    kernel_scores[kernel] = accuracy

# Output the optimal kernel function
best_kernel = max(kernel_scores, key=kernel_scores.get)
print("\nThe optimal kernel function is:", best_kernel)
