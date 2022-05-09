import numpy as np

# Su khac nhau chinh giua copy va view
# copy tao ra mot mang moi , con view chi la mot dang xem cua mang ban dau
#  bat ki thay doi nao tren mang  copy se khong anh huong den
# mang ban dau va nguoc lai
# View se khong so huu du lieu, bat ki thay doi view nao se anh huong den du lieu


arr = np.array([1, 2, 3, 4, 5])
x = arr.copy()
y = arr.view()

print(x.base) # mang copy tra ve none
print(y.base) # mang view tra ve mang ban dau
