import pandas as pd
import joblib
import os

# 获取当前脚本的目录路径
code_dir = os.path.dirname(os.path.abspath(__file__))

# 文件路径
X_test_file = os.path.join(code_dir, 'X_test.csv')  # 只包含特征的测试集
y_test_file = os.path.join(code_dir, 'y_test.csv')  # 只包含目标列的测试集
scaler_file = os.path.join(code_dir, 'scaler.joblib')
svm_model_file = os.path.join(code_dir, 'svm_model.joblib')

# 加载测试集的特征（X）和目标列（y）
X_test = pd.read_csv(X_test_file)
y_test = pd.read_csv(y_test_file)['Malignancy']  # 提取目标列

# 加载标准化器
scaler = joblib.load(scaler_file)

# 对测试数据进行标准化（使用训练时保存的标准化器）
X_test_scaled = scaler.transform(X_test)

# 加载 SVM 模型
svm_model = joblib.load(svm_model_file)

# 获取用户输入的测试数据索引
index = int(input("请输入要预测的测试样本索引（从 0 开始）: "))

# 根据输入的索引选择对应的测试样本
sample = X_test_scaled[index].reshape(1, -1)

# 进行预测
y_pred = svm_model.predict(sample)

# 预测结果映射
predicted_class = "良性" if y_pred[0] == 0 else "恶性"
true_class = "良性" if y_test.iloc[index] == 0 else "恶性"  # 使用索引获取真实类别

# 输出预测结果
print(f"预测的类别: {predicted_class}")
print(f"真实的类别: {true_class}")
A