import numpy
import matplotlib.pyplot as plt
numpy.random.seed(2)

x = numpy.random.normal(3, 1, 100)
y = numpy.random.normal(150, 40, 100) / x

train_x = x[:80]
train_y = y[:80]

test_x = x[80:]
test_y = y[80:]

mymodel= numpy.poly1d(numpy.polyfit(train_x, train_y, 4))
# tao mot mo hinh da thuc


myline= numpy.linspace(0, 6, 100)
# chi dinh cach dong hien thi bat dau o
# vi tri 0 va ket thuc o vi tri 6


plt.scatter(train_x, train_y)
# ve bieu do scatter du lieu train

plt.plot(myline, mymodel(myline))
# ve duong hoi quy da thuc

plt.show()
# hien thi bieu do