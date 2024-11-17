import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.preprocessing import StandardScaler
import os
import joblib

# 读取合并后的数据和已选择的特征
code_dir = os.path.dirname(os.path.abspath(__file__))
data_file = os.path.join(code_dir, '..', '2. Feature Extraction','3. Data preprocessing','refs', 'cleaned_data.csv')
selected_features_file = os.path.join(code_dir, '..', '2. Feature Extraction','4. Feature Selection','refs', 'selected_features.csv')

data_df = pd.read_csv(data_file)
selected_features_df = pd.read_csv(selected_features_file)


features = selected_features_df['Selected Features'].tolist()
X = data_df[features]
y = data_df['Malignancy']  # 确保 'Malignancy' 是目标变量

# 数据预处理：标准化
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# 保存标准化器
joblib.dump(scaler, 'scaler.joblib')

# 数据划分
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# 保存测试集的特征和目标数据到 CSV 文件
# 保存测试集的特征 (X) 到 CSV 文件，去掉目标列
test_features = pd.DataFrame(X_test, columns=features)  # 仅保存特征数据
test_features.to_csv(os.path.join(code_dir, 'X_test.csv'), index=False)
print("测试集特征已保存为 'X_test.csv'。")

# 保存测试集的目标列 (y) 到 CSV 文件
test_target = pd.DataFrame(y_test, columns=['Malignancy'])  # 保存目标列
test_target.to_csv(os.path.join(code_dir, 'y_test.csv'), index=False)
print("测试集目标列已保存为 'y_test.csv'。")


# 初始化 SVM 分类模型
svm_model = SVC(kernel='rbf', C=1.0, gamma='scale', random_state=42)  # 'rbf' 核函数

# 训练模型
svm_model.fit(X_train, y_train)

# 在测试集上进行预测
y_pred = svm_model.predict(X_test)

# 输出分类报告
print("分类报告:")
print(classification_report(y_test, y_pred))

# 输出混淆矩阵
print("混淆矩阵:")
print(confusion_matrix(y_test, y_pred))

# 保存模型
import joblib
joblib.dump(svm_model, 'svm_model.joblib')

print("SVM 模型训练完毕并已保存为 svm_model.joblib。")
