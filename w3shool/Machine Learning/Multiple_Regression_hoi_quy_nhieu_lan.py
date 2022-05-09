import pandas
# thu vien pandas cho phep lam viec voi file csv
# va tra ve mot doi tuong DataFrame
from sklearn import linear_model


df = pandas.read_csv("cars.csv")
# tra ve doi tuong DataFrame

X = df[['Weight', 'Volume']]
# tao mot danh sach cac gia tri doc lap goi la X

y = df['CO2']
# Dat cac gia tri phu thuoc vao bien y

# ***Mẹo: Người ta thường đặt tên cho danh sách
# các giá trị độc lập bằng chữ hoa X
# và danh sách các giá trị phụ thuộc bằng chữ hoa y.

regr = linear_model.LinearRegression()
# Từ mô-đun sklearn, chúng ta sẽ sử dụng
# LinearRegression()phương pháp này để
# tạo một đối tượng hồi quy tuyến tính.
# Đối tượng này có một phương thức được gọi là fit()

regr.fit(X, y)
# lấy các giá trị độc lập và phụ thuộc làm tham số
# và điền vào đối tượng hồi quy bằng dữ liệu mô tả
# mối quan hệ:

predictedCO2 = regr.predict([[2300, 1300]])
# Bây giờ chúng ta có một đối tượng hồi quy
# sẵn sàng dự đoán các giá trị CO2
# dựa trên trọng lượng và thể tích của một chiếc ô tô:

print(predictedCO2)
# dự đoán rằng một chiếc ô tô với động cơ 1,3 lít
# và trọng lượng 2300 kg, sẽ thải ra khoảng 107
#  gram CO2 cho mỗi km mà nó lái.

print(regr.coef_)
# in cac gia tri he so cua doi tuong hoi quy
# Mảng kết quả đại diện cho các giá trị 
# hệ số của trọng lượng và thể tích.
