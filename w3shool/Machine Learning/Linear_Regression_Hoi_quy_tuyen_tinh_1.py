import matplotlib.pyplot as plt
from scipy import stats

x = [89, 43, 36, 36, 95, 10, 66, 34, 38, 20,
     26, 29, 48, 64, 6, 5, 36, 66, 72, 40]
y = [21, 46, 3, 35, 67, 95, 53, 72, 58, 10,
     26, 34, 90, 33, 38, 20, 56, 2, 47, 15]
# thuc thi phuong thuc va tra ve gia tri chinh
slope, intercept, r, p, std_err = stats.linregress(x, y)

# Kết quả: r 0,013 chỉ ra mối quan
# hệ rất xấu và cho chúng ta biết
# rằng tập dữ liệu này không phù hợp với
# hồi quy tuyến tính.

# tao ham moi su dung 2 gia tri slope va intercept
# de tao ra gia tri moi. gia tri nay dai dien cho 
# truc y. gia tri x tuong ung se duoc dat vao 
def myfunc(x):
    return slope * x + intercept

# chay tung gia tri cua mang x thong qua ham.
# dieu nay dan den mot mang moi
# voi cac gia tri cho truc y 
mymodel = list(map(myfunc, x))

# ve bieu do phan tan ban dau
plt.scatter(x, y)

# ve duong hoi quy tuyen tinh
plt.plot(x, mymodel)

# hien thi do thi
plt.show()
