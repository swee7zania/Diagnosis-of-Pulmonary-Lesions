import pandas as pd
import joblib
import os
import warnings

# Block warning
warnings.filterwarnings("ignore", category=UserWarning, message=".*does not have valid feature names.*")

# Read test data and model
code_dir = os.path.dirname(os.path.abspath(__file__))
X_test_file = os.path.join(code_dir,'refs', 'X_test.csv') 
y_test_file = os.path.join(code_dir,'refs','y_test.csv') 
svm_model_file = os.path.join(code_dir, 'svm_rbf_model.joblib')

# Load the features (X) and target columns (y) of the test set
X_test = pd.read_csv(X_test_file)
y_test = pd.read_csv(y_test_file)['Malignancy']

# Loading the SVM model
svm_model = joblib.load(svm_model_file)

# Get the test data index entered by the user (starting from 2)
while True:
    try:
        index = int(input(f"Please enter the index of the test sample to predict (starting from 2): "))
        if index >= 2:
            break
        else:
            print("The index must be greater than or equal to 2. Please try again.")
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

# To correspond to the numbers in the left row of the CSV table, subtract 2 here because the data starts from the second row
sample = X_test.iloc[index - 2].values.reshape(1, -1)


# Print all feature data of the corresponding row
print(f"Feature data for the selected sample (Index {index}):")
print(X_test.iloc[index - 2])

# Making predictions
y_pred = svm_model.predict(sample)

# Prediction result mapping
predicted_class = "Benign" if y_pred[0] == 0 else "Malignant"
true_class = "Benign" if y_test.iloc[index - 2] == 0 else "Malignant"

# Output prediction results
print(f"Predicted result: {predicted_class}")
print(f"True result: {true_class}")
