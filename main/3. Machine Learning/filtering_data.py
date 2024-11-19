import os
import pandas as pd

# Read the merged data and selected features
code_dir = os.path.dirname(os.path.abspath(__file__))
data_file = os.path.join(code_dir, '..', '2. Feature Extraction','3. Data preprocessing','refs', 'cleaned_data.csv')
selected_features_file = os.path.join(code_dir, '..', '2. Feature Extraction','4. Feature Selection','refs', 'selected_features.csv')

cleaned_data = pd.read_csv(data_file)
selected_features = pd.read_csv(selected_features_file)["Selected Features"].tolist()
# Add label column to features list
selected_features.append("Malignancy")
# Filter out the extracted features and label columns
filtered_data = cleaned_data[selected_features]
# Save as a new CSV file
filtered_data.to_csv(os.path.join(code_dir, 'refs', 'filtered_data.csv'), index=False)