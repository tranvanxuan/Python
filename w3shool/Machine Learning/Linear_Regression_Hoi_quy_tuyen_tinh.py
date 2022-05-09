import matplotlib.pyplot as plt
from scipy import stats

x = [5, 7, 8, 7, 2, 17, 2, 9, 4, 11, 12, 9, 6]
y = [99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86]

# thuc thi phuong thuc va tra ve gia tri chinh cua hoi quy tuyen tinh
slope, intercept, r, p, std_err = stats.linregress(x, y)

# Lưu ý: Kết quả -0,76 cho thấy rằng có
# một mối quan hệ, không phải là hoàn hảo,
# nhưng nó chỉ ra rằng chúng ta có thể
# sử dụng hồi quy tuyến tính trong
# các dự đoán trong tương lai.

# Tạo một hàm sử dụng slope và interceptgiá trị
# để trả về một giá trị mới. Giá trị mới này
# đại diện cho vị trí trên trục y, giá trị x
# tương ứng sẽ được đặt


def myfunc(x):
    return slope * x + intercept


# Chạy từng giá trị của mảng x thông qua hàm.
# Điều này sẽ dẫn đến một mảng mới
# với các giá trị mới cho trục y:
mymodel = list(map(myfunc, x))

# Vẽ biểu đồ phân tán ban đầu:
plt.scatter(x, y)

# Vẽ đường hồi quy tuyến tính:
plt.plot(x, mymodel)

# Hiển thị sơ đồ:
plt.show()
