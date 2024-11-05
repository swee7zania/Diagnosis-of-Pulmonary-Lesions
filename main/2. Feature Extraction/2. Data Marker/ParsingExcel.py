import pandas as pd
import os

# 设置路径
code_dir = os.path.dirname(os.path.abspath(__file__))
excel_file_path = os.path.join(code_dir,'refs', 'MetadatabyAnnotation.xlsx')

# 读取 Excel 数据
data = pd.read_excel(excel_file_path)

# 提取 Patient ID 和 Malignancy 列
labels_dict = data.set_index('patient_id')['Malignancy'].to_dict()

# 定义恶性程度到分类的映射
def classify_malignancy(malignancy):
    if malignancy in ["Highly Suspicious", "Moderately Suspicious"]:
        return "Malignant"
    elif malignancy in ["Highly Unlikely", "Moderately Unlikely"]:
        return "Benign"
    else:  # Indeterminate
        return "Indeterminate"

# 遍历标签字典并生成分类
classification_results = []

for patient_id, malignancy in labels_dict.items():
    classification = classify_malignancy(malignancy)
    classification_results.append((patient_id, malignancy, classification))

# 打印结果
# for result in classification_results:
#     print(f"Patient ID: {result[0]}, Malignancy: {result[1]}, Classification: {result[2]}")

# 如果需要，可以将结果保存为新的 Excel 文件
classification_df = pd.DataFrame(classification_results, columns=['Patient ID', 'Malignancy', 'Classification'])
output_excel_path = os.path.join(code_dir,'refs', 'malignancy_classification.csv')
classification_df.to_csv(output_excel_path, index=False)
print(f"Classification results saved to: {output_excel_path}")