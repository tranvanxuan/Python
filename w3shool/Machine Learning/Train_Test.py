import numpy

import matplotlib.pyplot as plt

x = numpy.random.normal(3, 1, 100)
y = numpy.random.normal(150, 40, 100) / x


train_x = x[:80]
train_y = y[:80]
# Tập huấn luyện phải là sự lựa chọn ngẫu nhiên của 80% dữ liệu gốc.

test_x = x[80:]
test_y = y[80:]

# Bộ thử nghiệm nên là 20% còn lại.

# plt.scatter(x, y)
#  ve bieu do phan tan du lieu goc

# plt.scatter(train_x, train_y)
# # ve bieu do phan tan du lieu traning

plt.scatter(test_x, test_y)
# ve bieu do phan tan du lieu test

plt.show()
# hien thi bieu do
