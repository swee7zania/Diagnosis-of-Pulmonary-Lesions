# Diagnosis-of-Pulmonary-Lesions

> 1. I suggest expressing in the third person to facilitate distinguishing the author of each update;
>
> 2. The version number starts with a step (for example, in the first step of segmentation, the first digit of the version number is `1.x.x`);

### Version 1.0.0

1. ##### Updated folder structure

     - `Liu Zhihan` placed the code part in ‘main’ folder and the dataset in DATASET;
     - In the ‘main’ folder, I have divided each step into folders with numbers to display the steps more clearly;

2. ##### Submitted Segmentation.py

     - `Liu Zhihan` submitted the code and marked the modified parts with """comments""";

     - Mainly updated the import of datasets and the output of comparison images after segmentation;


### Version 1.0.1

1. **Added save folder**

     - `Liu Zhihan` added the folder of saving files, which is mainly used to save the segmented data;
     - I saved it in the OUTPUT_SEGMENTED folder at the same level as VOIs;

2. **Updated segmentation code**

   - `Liu Zhihan` updated the segmentation code, now it can process data in batches;
   - Modified the method of reading .nii.gz, now use `nibabel` to read the file;

3. **Submitted visualize_segmented.py**

     - `Liu Zhihan` submitted the code and marked the modified parts with #comments;

     - Mainly used to verify whether the segmented data is saved correctly;
