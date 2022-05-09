import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# import toan bo file univariate
_X = np.loadtxt('multivariate.txt', delimiter=',')

# import theta tu file univaiate_theta.txt
Theta = np.loadtxt('multivariate_theta.txt')


# chuyen cot dau tien sang cot 2
X = np.zeros((np.size(_X, 0), np.size(_X, 1)))

# them cot dau bang 1
X[:, 0] = 1

n = np.size(_X, 1) - 1
X[:, 1:] = _X[:, 0:n]

# luu co y lai
y = np.copy(X[:, -1])

# tinh loi nhuan (don vi 10000$)
predict = X@Theta


# in bộ diện tích-số phòng-giá đầu tiên
print('%.2f feet-vuông, %d phòng ngủ : %.1f$' % (X[0, 1], X[0, 2], predict[0]))
# luu file
np.savetxt('predict_value.txt', predict, fmt='%.6f')

# plot gia tri thuc te khong lay cot bias 1 dau
# X[:,1:] la x-axis cua bieu do, khong lay cot dau:
# y la y-axis , rx la red x, plot du lieu bang dau x mau do
plt.scatter(X[:, 1:], y)

plt.plot(predict/10000, y, '-b')

# hien thi bieu do
plt.show()
