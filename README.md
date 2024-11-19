# Diagnosis-of-Pulmonary-Lesions

> 1. I suggest expressing in the third person to facilitate distinguishing the author of each update;
>
> 2. The version number starts with a step (for example, in the first step of segmentation, the first digit of the version number is `1.x.x`);
>
> 3. When submitting code to GitHub, please commit the author and version.



### Version 1.0.0

1. ##### Updated folder structure

     - `Liu Zhihan` placed the code part in ‘main’ folder and the dataset in DATASET;
     - In the ‘main’ folder, I have divided each step into folders with numbers to display the steps more clearly;

2. ##### Submitted Segmentation.py

     - `Liu Zhihan` submitted the code and marked the modified parts with """comments""";
- Mainly updated the import of datasets and the output of comparison images after segmentation;



------

### Version 1.0.1

1. **Added save folder**
     - `Liu Zhihan` added the folder of saving files, which is mainly used to save the segmented data;
     - I saved it in the OUTPUT_SEGMENTED folder at the same level as VOIs;
2. **Updated segmentation code**

   - `Liu Zhihan` updated the `segmentation.py` code, now it can process data in batches;
   - Modified the method of reading .nii.gz, now use `nibabel` to read the file;
3. **Submitted visualize_segmented.py**

     - `Liu Zhihan` submitted the code and marked the modified parts with #comments;
- Mainly used to verify whether the segmented data is saved correctly;



------

### Version 2.0.0

1. **Carry out Feature Extraction**
   - `Liu Zhihan`  chose `PyRadiomics` for feature extraction, and updated the `featuresExtraction.py` code;
   - Due to hardware limitations, data will be processed in batches, and note I will write in the `.py` file;
   - The extracted feature data is stored in `refs -> extracted_features.csv`;
2. **Label the data (malignant/benign)**
   - `Liu Zhihan`  wrote the judgment criteria mentioned in the data set in `Tag classification description.md`;
   - Updated `ParsingExcel.py` code to store the marked data in `refs -> malignancy_classification.csv`;
3. **Data preprocessing**
   - `Liu Zhihan` merged `extracted_features.csv` and `malignancy_classification.csv`;
   - Updated `MergeData.py` code to store the marked data in `refs -> merged_data.csv`;
   - This is the basis for feature selection;



------

### Version 2.0.1

1. **Choose a feature selection method**
   - `Liu Zhihan`  chose the `mRMR` method;
   - The comparison of the two methods is written in `Two methods of feature selection.md`;
2. **Data preprocessing**
   - `Liu Zhihan` preprocessed the merged data.
   - The `mRMR` algorithm is only for numerical features.
   - Updated `PreprocessingData.py` code to store the marked data in `refs -> cleaned_data.csv`;
3. **Feature selection**
   - `Liu Zhihan` extracted the first ten features using the `mRMR` method;
   - Updated `mRMR_feature_selection.py` code to store the marked data in `refs -> selected_features.csv`;
   - If you want to run it, you need to install the corresponding library `pip install mrmr_selection`;

------

### Version 3.0.0

1. **Machine Learning**
   - `Liu Zhihan`  uses SVM for machine learning;
   - The final model and normalizer are saved;
   - The test set is saved for testing, in `X_test.csv` and `y_test.csv`;
2. **Testing the Model**
   - `Liu Zhihan` updated the `predict_lesion_svm.py` code for testing the model;
   - Allows users to input which test data to use for testing;
   

### Version 3.0.1

> Major update, marking the end. I put the most detailed steps in `3. Machine Learning -> Steps.md`

1. **Comparing Different Models**
   - `Liu Zhihan` uses the K-fold method to fold 5 times and compares the two machine training models of SVM and KNN;
   - Finally, it is concluded that SVM is the best method;

2. **Comparing Different Kernel Functions**
   - `Liu Zhihan` compares different kernel functions in the SVM algorithm;
   - The final result is that RBF is the optimal function;

3. **Testing the Model**

   - `Liu Zhihan` training SVM method using RBF kernel function;

   - The final model is saved in `svm_rbf_model.joblib`, with an accuracy of about 75%;
   - At the same time, the test set data is also saved for testing;

4. **Using the Model**

   - `Liu Zhihan` updates `zpredict_lesion_svm.py` code for use in the final model;
   - Use the saved test set data for testing. The user enters the serial number of the test row to get the prediction result.

   
