import numpy as np
import matplotlib.pyplot as plt  # thu vien ve bieu do
from functions import*

# import toan bo file data.txt
raw = np.loadtxt('data.txt', delimiter=',')

# tach lay X
X = np.copy(raw)
X[:, 1] = X[:, 0]
# them bias 1
X[:, 0] = 1
# tach lay y
y = raw[:, 1]
# Train data
[Theta, J_hist] = GradientDescent(X, y)
# Predict
predict = predict(X, Theta) * 10000  # chuyển về đơn vị người
# Plot kết quả
plt.figure(1)
plt.plot(X[:, 1], y, 'rx')
plt.plot(X[:, 1], predict/10000, '-b')  # đơn vị gốc: nghìn người
plt.figure(2)
plt.plot(J_hist[:, 0], J_hist[:, 1], '-r')
plt.show()  # chỉ gọi 1 lần trong chương trình để hiển thị các biểu đồ cùng lúc
plt.show()  # nếu bạn muốn vẽ thêm biểu đồ J(θ), hàm show được gọi sau khi vẽ biểu đồ J(θ)
