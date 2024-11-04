import os
import nibabel as nib
from tools.VolumeCutBrowser import VolumeCutBrowser

# Set the file path
code_dir = os.path.dirname(os.path.abspath(__file__))
input_dir = os.path.abspath(os.path.join(code_dir, '..', '..', 'DATASET')) 
OutputFolder = 'OUTPUT_SEGMENTED'
file_name = 'LIDC-IDRI-0001_R_1_segmented.nii.gz'  # 根据实际文件名修改
segmented_file_path = os.path.join(input_dir, OutputFolder, 'image', file_name)

# Check if a file exists
if not os.path.isfile(segmented_file_path):
    raise FileNotFoundError(f"Segmented file '{segmented_file_path}' not found.")

# Read the segmented image
nii_seg_img = nib.load(segmented_file_path)
niiROISeg = nii_seg_img.get_fdata()

# Display the segmented image
VolumeCutBrowser(niiROISeg)
