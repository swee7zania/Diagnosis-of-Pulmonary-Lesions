# feature_extraction.py

# 导入必要的库
import numpy as np
from skimage.measure import regionprops, label
import nibabel as nib
import os
import json  # 用于保存特征数据


#### Data Folders
"""
    Author: LIU ZHIHAN
    Function: Set the relative path to the code and data folders
"""
code_dir = os.path.dirname(os.path.abspath(__file__))
SessionDataFolder = os.path.abspath(os.path.join(code_dir, '..', '..', 'DATASET')) 


CaseFolder='VOIs'
NiiFile='LIDC-IDRI-0001_R_1.nii.gz'
# 设定数据路径
segmentation_file_path = os.path.join(SessionDataFolder,CaseFolder,'image',NiiFile)  # 替换为实际的分割结果路径
original_image_path = os.path.join('..', 'data', 'original_ct_image.nii.gz')  # 替换为实际的原始CT图像路径

# 特征提取函数
def extract_features(segmented_image, original_image):
    # 使用 `label` 对病变区域进行标记
    labeled_image = label(segmented_image)
    # 使用 `regionprops` 从标记图像和原始图像中提取特征
    properties = regionprops(labeled_image, intensity_image=original_image)
    
    features = []
    # 遍历每个病变区域，提取所需的特征
    for prop in properties:
        features.append({
            'area': prop.area,  # 病变区域面积
            'eccentricity': prop.eccentricity,  # 离心率
            'solidity': prop.solidity,  # 密度
            'mean_intensity': prop.mean_intensity  # 平均强度
        })
    
    return features

# 1. 加载分割结果和原始CT图像
# 使用nibabel库读取分割图像
nii_seg = nib.load(segmentation_file_path)
nii_roi = nib.load(original_image_path)

# 将图像数据提取为数组
segmented_image = nii_seg.get_fdata()  # 分割后的二值图像
original_image = nii_roi.get_fdata()   # 原始CT图像

# 2. 提取特征
features = extract_features(segmented_image, original_image)

# 3. 保存特征数据
# 假设标签已知，且为列表格式 `labels`（良性0，恶性1）
# 替换 `labels` 为你实际的标签
labels = [0, 1]  # 示例标签

# 将特征和标签打包成结构化数据
data = {
    'features': features,
    'labels': labels
}

# 保存到JSON文件，供分类使用
output_path = os.path.join('..', 'data', 'features.json')
with open(output_path, 'w') as f:
    json.dump(data, f, indent=4)

print(f"Features extracted and saved to {output_path}")
