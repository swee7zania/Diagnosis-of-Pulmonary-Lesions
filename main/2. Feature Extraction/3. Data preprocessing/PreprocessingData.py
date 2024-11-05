import pandas as pd
import os

"""
    Author: LIU ZHIHAN
    Function: Preprocess the merged data, The mRMR algorithm is only for numerical features
"""

code_dir = os.path.dirname(os.path.abspath(__file__))
merged_file = os.path.join(code_dir, 'refs', 'merged_data.csv')

# Read the merged data
merged_data = pd.read_csv(merged_file)

# Check data types
# print(merged_data.dtypes)

# Remove non-numerical feature columns
# The 'Patient ID' and 'Malignancy' columns are retained, and the other columns need to be numeric
features = merged_data.select_dtypes(include=['float64', 'int64']).columns.tolist()

# Preserve feature and label data
cleaned_data = merged_data[features]

# Display the first two rows of cleaned data
# print(cleaned_data.head())

# Save the cleaned data format
cleaned_data.to_csv(os.path.join(code_dir, 'refs', 'cleaned_data.csv'), index=False)
print("The cleaned data has been saved successfully")
