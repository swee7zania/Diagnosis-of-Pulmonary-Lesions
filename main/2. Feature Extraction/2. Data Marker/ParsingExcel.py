import pandas as pd
import os

"""
    Author: LIU ZHIHAN
    Function: Label the data as malignant or benign
"""
code_dir = os.path.dirname(os.path.abspath(__file__))
excel_file_path = os.path.join(code_dir,'refs', 'MetadatabyAnnotation.xlsx')

# Reading Excel data
data = pd.read_excel(excel_file_path)

# Extract the Patient ID and Malignancy columns
labels_dict = data.set_index('patient_id')['Malignancy'].to_dict()

# Define the mapping from malignancy to classification
def classify_malignancy(malignancy):
    if malignancy in ["Highly Suspicious", "Moderately Suspicious"]:
        return "Malignant"
    elif malignancy in ["Highly Unlikely", "Moderately Unlikely"]:
        return "Benign"
    else:  # Indeterminate
        return "Indeterminate"

# Traverse the label dictionary and generate categories
classification_results = []

for patient_id, malignancy in labels_dict.items():
    classification = classify_malignancy(malignancy)
    classification_results.append((patient_id, malignancy, classification))

# Printing Results
# for result in classification_results:
#     print(f"Patient ID: {result[0]}, Malignancy: {result[1]}, Classification: {result[2]}")

# Save the results as a new Excel file
classification_df = pd.DataFrame(classification_results, columns=['Patient ID', 'Malignancy', 'Classification'])
output_excel_path = os.path.join(code_dir,'refs', 'malignancy_classification.csv')
classification_df.to_csv(output_excel_path, index=False)
print(f"Classification results saved to: {output_excel_path}")