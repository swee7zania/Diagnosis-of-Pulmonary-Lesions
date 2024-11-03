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
from NiftyIO import readNifty
# Volume Visualization
from VolumeCutBrowser import VolumeCutBrowser


######## LOAD DATA

#### Data Folders
"""
    Author: LIU ZHIHAN
    Function: Set the relative path to the code and data folders
"""
code_dir = os.path.dirname(os.path.abspath(__file__))
SessionDataFolder = os.path.abspath(os.path.join(code_dir, '..', '..', 'DATASET')) 

if not os.path.isdir(SessionDataFolder):
    raise FileNotFoundError(f"Data directory '{SessionDataFolder}' not found.")

os.chdir(SessionDataFolder)


CaseFolder='VOIs'
NiiFile='LIDC-IDRI-0001_R_1.nii.gz'


#### Load Intensity Volume
NiiFile=os.path.join(SessionDataFolder,CaseFolder,'image',NiiFile)
niiROI,niimetada=readNifty(NiiFile)


######## VISUALIZE VOLUMES

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
niiROISeg=niiROI>Th
# ROI Histogram
fig,ax=plt.subplots(1,1)
ax.hist(niiROI.flatten(),bins=50,edgecolor='k')

"""
    Author: LIU ZHIHAN
    Function: Display histogram, original image and segmented image
"""
plt.title('Intensity Histogram')
plt.xlabel('Intensity Value')
plt.ylabel('Frequency')
plt.show()  # 显示直方图

VolumeCutBrowser(niiROI)  # 显示原始图像
VolumeCutBrowser(niiROISeg)  # 显示分割后的图像

# 检查二值化输出
"""
    Author: LIU ZHIHAN
    Function: Display the before and after comparison of slices
"""
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


### 3.POST-PROCESSING

# 3.1  Opening 
szeOp=3
se=Morpho.cube(szeOp)
niiROISegOpen = Morpho.binary_opening(niiROISeg, se)

# 3.2  Closing 
szeCl=3
se=Morpho.cube(szeCl)
niiROISegClose = Morpho.binary_closing(niiROISeg, se)

