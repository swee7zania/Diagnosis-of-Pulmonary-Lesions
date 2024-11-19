### **Step 1: Data Filtering and Saving (Filtering Data)**

* In the first step, the raw input data is cleaned and filtered. This process involves removing irrelevant features, handling missing values, and performing other necessary data cleaning tasks. The filtered data is saved as `refs/filtered_data.csv` and serves as input for the following steps.

**File saved as**:
* `refs/filtered_data.csv`

---

### **Step 2: KFold Cross-Validation (KFold Verification)**

* In this step, KFold cross-validation is used to split and train the data. This process ensures that the model is trained and validated on different subsets of the data, improving the model's generalizability. Both SVM and KNN models are validated, and the results of each fold are outputted to determine the best model performance.

**Output**:
* KFold cross-validation results: A comparison of model performance across folds to help select the most suitable machine learning method.

---

### **Step 3: SVM Kernel Function Comparison (SVM Kernel Comparison)**

* After confirming SVM as the optimal model, this step compares different SVM kernel functions (such as `sigmoid`, `poly`, and `rbf`) to select the best one. Model performance is evaluated using classification reports (precision, recall, F1 score, etc.). Ultimately, the `rbf` kernel function is selected as the optimal choice.

**Output**:
* Performance comparison of different SVM kernel functions.
* Selection of the best kernel (`rbf`) for the final model training.

---

### **Step 4: SVM Model Training and Saving (SVM RBF Training)**

* In this step, the SVM model is trained using the selected `rbf` kernel, and the trained model is saved as `svm_rbf_model.joblib`. Additionally, the feature data and target data for the test set are saved as `refs/X_test.csv` and `refs/y_test.csv`, respectively, for future analysis and predictions.

**Output**:
* Trained SVM model: `svm_rbf_model.joblib`
* Test set feature data: `refs/X_test.csv`
* Test set target label data: `refs/y_test.csv`

---

### **Step 5: Predict Using the Trained Model (Predict Using SVM)**

* In this step, new test data is input, and the trained SVM model (`svm_rbf_model.joblib`) is used to predict the lesion status. The results are generated based on the row numbers corresponding to the test data from the second row in the CSV file to ensure the correct mapping.

**Output**:
* Prediction results: Compare the predictions based on the input data in `X_test.csv`.

---

### **第一步：数据过滤与保存 (Filtering Data)**

* 在第一步中，输入的原始数据被清洗和过滤。该过程包括去除无关特征、处理缺失值以及进行其他必要的数据清理。过滤后的数据存储为 `refs/filtered_data.csv`，并作为后续步骤的输入。

**文件保存位置**:
* `refs/filtered_data.csv`

---

### **第二步：KFold交叉验证 (KFold Verification)**

* 在这一阶段，使用KFold交叉验证对数据进行分割和训练。此过程确保了模型在不同的数据子集上进行训练和验证，从而提高模型的泛化能力。我们使用SVM和KNN两种模型进行验证，并输出每一折的验证结果，最后得出最优模型的性能。

**输出**:
* KFold交叉验证结果：交叉验证后的模型性能对比，帮助选择最合适的机器学习方法。

---

### **第三步：SVM核函数比较 (SVM Kernel Comparison)**

* 在确定SVM作为最优模型后，本步骤通过比较不同的SVM核函数（如 `sigmoid`, `poly`, `rbf`）来选择最佳的核函数。模型性能通过分类报告（精度、召回率、F1分数等指标）来评估。最终，选择 `rbf` 核函数作为最优核函数。

**输出**:
* 各种SVM核函数的性能对比报告。
* 选择最佳核函数（`rbf`）用于最终的模型训练。

---

### **第四步：SVM模型训练与保存 (SVM RBF Training)**

* 使用选定的 `rbf` 核函数训练SVM模型，并将训练好的模型保存为 `svm_rbf_model.joblib`。此外，测试集的特征和目标数据分别保存为 `refs/X_test.csv` 和 `refs/y_test.csv`，以便后续分析和预测使用。

**输出**:
* 训练好的SVM模型：`svm_rbf_model.joblib`
* 测试集特征数据：`refs/X_test.csv`
* 测试集目标标签数据：`refs/y_test.csv`

---

### **第五步：使用训练好的模型进行预测 (Predict Using SVM)**

* 在这一步，通过输入新的测试集数据，使用训练好的 SVM 模型（`svm_rbf_model.joblib`）进行病变预测。预测的结果根据给定行号（从CSV表格的第二行开始）生成，确保测试集的行号与预测对应。

**输出**:
* 预测结果：根据 `X_test.csv` 中的输入数据，对比预测结果。