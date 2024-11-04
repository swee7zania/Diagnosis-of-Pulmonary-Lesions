"""
This is the source code for volume visualization

Computer Vision Center
Universitat Autonoma de Barcelona

__author__ = "Debora Gil, Guillermo Torres, Carles Sanchez, Pau Cano"
__license__ = "GPL"
__email__ = "debora,gtorres,csanchez,pcano@cvc.uab.es"
__year__ = "2023"
"""

### IMPORT PY LIBRARIES
# Python Library 2 manage volumetric data
import numpy as np
# Pyhton standard Visualization Library
import matplotlib.pyplot as plt
# Pyhton standard IOs Library
import os
# Basic Processing
from skimage.filters import threshold_otsu
from skimage import morphology as Morpho
from scipy.ndimage import gaussian_filter, median_filter
# .nii Read Data
from tools.NiftyIO import readNifty
# Volume Visualization
from tools.VolumeCutBrowser import VolumeCutBrowser
# Save segmentation results
import nibabel as nib


######## LOAD DATA

#### Data Folders
"""
    Author: LIU ZHIHAN
    Function: Set the relative path to the code and data folders
    Update: Created a folder for storing split files
"""
code_dir = os.path.dirname(os.path.abspath(__file__))
input_dir = os.path.abspath(os.path.join(code_dir, '..', '..', 'DATASET')) 

if not os.path.isdir(input_dir):
    raise FileNotFoundError(f"Data directory '{input_dir}' not found.")

os.chdir(input_dir)

CaseFolder = 'VOIs'
OutputFolder = 'OUTPUT_SEGMENTED'
image_folder = os.path.join(input_dir, CaseFolder, 'image')
output_folder = os.path.join(input_dir, OutputFolder, 'image')

os.makedirs(output_folder, exist_ok=True)  # Create Output Folder


"""
    Author: LIU ZHIHAN
    Function: Traverse over each .nii.gz file in the dataset folder
"""
for filename in os.listdir(image_folder):
    if filename.endswith('.nii.gz'):
        input_path = os.path.join(image_folder, filename)
        # print(f"Processing file: {input_path}")
        
        # Load the.nii.gz file using nibabel
        nii_img = nib.load(input_path)  # 加载 Nifti 图像
        niiROI = nii_img.get_fdata()  # 获取图像数据
        affine = nii_img.affine  # 获取仿射矩阵
        
        ######## SEGMENTATION PIPELINE
        """
            Modifier: LIU ZHIHAN
            Reason: scipy.ndimage.filters namespace is deprecated
                    IMSeg parameter format is not supported
        """
        ### 1. PRE-PROCESSING
        # 1.1 Gaussian Filtering
        sig=1
        niiROIGauss = gaussian_filter(niiROI, sigma=sig)
        # 1.2 MedFilter
        sze=3
        niiROIMed = median_filter(niiROI, sze)
        ###
        
        ### 2. BINARIZATION
        Th = threshold_otsu(niiROI)
        niiROISeg = niiROI > Th
        
        """
            Author: LIU ZHIHAN
            Function: Display histogram, original image and segmented image
            Update: I did a batch process so I didn't need to open each image for display
        """
        """
            # ROI Histogram
            fig,ax=plt.subplots(1,1)
            ax.hist(niiROI.flatten(),bins=50,edgecolor='k')
            # 显示直方图
            plt.title('Intensity Histogram')
            plt.xlabel('Intensity Value')
            plt.ylabel('Frequency')
            plt.show() 
            
            VolumeCutBrowser(niiROI)  # 显示原始图像
            VolumeCutBrowser(niiROISeg)  # 显示分割后的图像
        """
        
        """
            Author: LIU ZHIHAN
            Function: Display the before and after comparison of slices
            Update: I did a batch process so I didn't need to open each image for display
        """
        """
            # 检查二值化输出
            slice_index = niiROISeg.shape[2] // 2  # 获取中间切片
            plt.figure(figsize=(10, 5))
            # 显示原始切片
            plt.subplot(1, 2, 1)
            plt.imshow(niiROI[:, :, slice_index], cmap='gray')
            plt.title('Original Image Slice')
            plt.axis('off')
            # 显示分割切片
            plt.subplot(1, 2, 2)
            plt.imshow(niiROISeg[:, :, slice_index], cmap='gray')
            plt.title('Segmented Image Slice')
            plt.axis('off')
            plt.show()  # 显示切片图像
        """
        
        ### 3.POST-PROCESSING
        # 分割图像中可能存在一些噪声或不完整的区域，后处理步骤可以对这些区域进行平滑、填补，进一步提升分割效果的质量。
        # 这里具体用了形态学操作中的“开运算”和“闭运算”。
        # 3.1  Opening 
        szeOp=3
        se=Morpho.cube(szeOp)
        niiROISegOpen = Morpho.binary_opening(niiROISeg, se)
        
        # 3.2  Closing 
        szeCl=3
        se=Morpho.cube(szeCl)
        niiROISegClose = Morpho.binary_closing(niiROISeg, se)
        
        """
            Author: LIU ZHIHAN
            Function: Used to save the segmented image to the specified folder
        """
        # 4.SAVE SEGMENTATION RESULTS
        output_path = os.path.join(output_folder, filename.replace('.nii.gz', '_segmented.nii.gz'))
        nii_seg_img = nib.Nifti1Image(niiROISegClose.astype(np.uint8), affine)
        nib.save(nii_seg_img, output_path)
        print(f"Segmented data saved to {output_path}")

