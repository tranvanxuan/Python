import numpy as np
import matplotlib.pyplot as plt
# nhap cac modul ban can

x = [1, 2, 3, 5, 6, 7, 8, 9, 10, 12, 13, 14, 15, 16, 18, 19, 21, 22]
y = [100, 90, 80, 60, 60, 55, 60, 65, 70, 70, 75, 76, 78, 79, 90, 99, 99, 100]
# tao cac mang dai dien cho cac truc x, y

mymodel = np.poly1d(np.polyfit(x, y, 3))
# phuong thuc tao mot mo hinh da thuc


myline = np.linspace(1, 22, 100)
# chi dinh cach dong hien thi. 
# bat dau o vi tri 1 va ket thuc o vi tri 22

plt.scatter(x, y)
# ve  bieu do phan tan ban dau

plt.plot(myline, mymodel(myline))
# ve duong hoi quy da thuc

plt.show()
# hien thi bieu do
