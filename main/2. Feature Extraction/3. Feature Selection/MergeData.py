import pandas as pd
import os
import pymrmr

"""
    Author: LIU ZHIHAN
    Function: Extract features from the segmented data and select some features to record in Excel
    Attention: Please make sure the dependent libraries are installed before runnin - pymrmr
"""

code_dir = os.path.dirname(os.path.abspath(__file__))
features_file = os.path.join(code_dir, '..', '1. PyRadiomics', 'refs', 'extracted_features.csv') # 包含特征数据的CSV文件
labels_file = os.path.join(code_dir, '..', '2. Data Marker', 'refs', 'malignancy_classification.csv') # 包含标签数据的CSV文件（Patient ID和Malignancy）

# Read feature data and tag data
feature_df = pd.read_csv(features_file)
label_df = pd.read_csv(labels_file)

# Merging feature and label data
data_df = pd.merge(feature_df, label_df[['Patient ID', 'Malignancy']], on='Patient ID')

# Convert the “Malignancy” column to binary labels (1 for malignant and 0 for benign)
data_df['Malignancy'] = data_df['Malignancy'].apply(lambda x: 1 if x in ['Highly Suspicious', 'Moderately Suspicious'] else 0)

# Save the merged data
data_df.to_csv(os.path.join(code_dir, 'refs', 'merged_data.csv'), index=False)
print("The merged data has been successfully saved.")
