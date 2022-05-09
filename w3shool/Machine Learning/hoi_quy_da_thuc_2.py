import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score
# nhap cac modul ban can

x = [1, 2, 3, 5, 6, 7, 8, 9, 10, 12, 13, 14, 15, 16, 18, 19, 21, 22]
y = [100, 90, 80, 60, 60, 55, 60, 65, 70, 70, 75, 76, 78, 79, 90, 99, 99, 100]
# tao cac mang dai dien cho cac truc x, y

mymodel = np.poly1d(np.polyfit(x, y, 3))
# phuong thuc tao mot mo hinh da thuc

print(r2_score(y, mymodel(x)))
# Lưu ý: Kết quả 0,94 cho thấy có một
# mối quan hệ rất tốt và chúng ta có thể
#  sử dụng hồi quy đa thức trong các dự đoán
#  trong tương lai.

speed = mymodel(17)
# du doan toc do cua mot chiec o to luc 17h chieu

print(speed)