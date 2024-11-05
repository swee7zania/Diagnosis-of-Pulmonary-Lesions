import pandas as pd
from mrmr import mrmr_classif
import os

"""
    Author: LIU ZHIHAN
    Function: Extract features from the segmented data and select some features to record in Excel
    Attention: Please make sure the dependent libraries are installed before runnin - mrmr_selection
"""
code_dir = os.path.dirname(os.path.abspath(__file__))
data_file = os.path.join(code_dir, '..', '3. Data preprocessing','refs', 'cleaned_data.csv')
data = pd.read_csv(data_file)

# Extracting features and target variables
X = data.drop(columns=['Malignancy'])
y = data['Malignancy']

# Perform mRMR feature selection
selected_features = mrmr_classif(X, y, K=10)  # Select the top 10 features

# Output selected features
print("Selected features:", selected_features)

# Save selected features to a CSV file
selected_features_df = pd.DataFrame(selected_features, columns=['Selected Features'])
selected_features_df.to_csv(os.path.join(code_dir,'refs','selected_features.csv'), index=False)

print("Features have been successfully selected and saved")