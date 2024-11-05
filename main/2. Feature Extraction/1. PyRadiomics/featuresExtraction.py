import os
import pandas as pd 
import SimpleITK as sitk
from radiomics import featureextractor
from radiomics import setVerbosity

"""
    Author: LIU ZHIHAN
    Function: Extract features from the segmented data and select some features to record in Excel
    Attention: Since the dataset is too large, I will process it in batches. Please wait patiently.
               When "Feature extraction completed" appears, the processing is complete.
"""
# Set the file path
code_dir = os.path.dirname(os.path.abspath(__file__))
input_dir = os.path.abspath(os.path.join(code_dir, '..', '..', '..', 'DATASET')) 
OutputFolder = 'OUTPUT_SEGMENTED'

# Image directory and mask directory
image_file_path = os.path.join(input_dir, OutputFolder, 'image') # 存放医学图像的文件夹
mask_file_path = os.path.join(input_dir, OutputFolder, 'nodule_mask') # 存放对应掩码（肺结节标记）的文件夹

# Create a feature storage data frame
feature_data = []

# Initialize the feature extractor
params = 'config/Params.yaml'
extractor = featureextractor.RadiomicsFeatureExtractor(params)

# Iterate through all image files in the images folder
image_files = [f for f in os.listdir(image_file_path) if f.endswith('.nii.gz')]

# Process the data in five steps
n = len(image_files)
batch_size = n // 5 + (1 if n % 5 != 0 else 0)  # 计算每批处理的数量

for batch in range(5):
    start = batch * batch_size
    end = start + batch_size
    print(f"Processing batch {batch + 1}: images {start + 1} to {min(end, n)}")

    for i in range(start, min(end, n)):
        image_file = image_files[i]
        mask_file = image_file.replace('_segmented', '')  # 生成对应掩码文件名
        patient_id = image_file.split('_')[0]  # 提取Patient ID

        # 读取图像和掩码
        imageITK = sitk.ReadImage(os.path.join(image_file_path, image_file))
        maskITK = sitk.ReadImage(os.path.join(mask_file_path, mask_file))

        try:
            # 提取特征
            feature_vector = extractor.execute(imageITK, maskITK)
            feature_vector['Patient ID'] = patient_id  # 添加Patient ID
            # 将特征结果添加到数据框中
            feature_data.append(feature_vector)
            # print(f"成功提取特征: {image_file} 和 {mask_file}")

        except Exception as e:
            print(f"提取特征时出错: {e}")

# Save the extracted feature data to a CSV file
features_df = pd.DataFrame(feature_data)
features_df.to_csv(os.path.join(code_dir,'refs', 'extracted_features.csv'), index=False)

print("Feature extraction completed, results saved to 'refs/extracted_features.csv'。")