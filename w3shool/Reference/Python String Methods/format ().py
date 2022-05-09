# phuong thuc format () dinh dang mot gia tri cu the, va chen chung vao (trinh du cho cua chuoi-dau ngoac {} cua chuoi.)

txt= "For only {price:.2f} dollars!"
# chen 49 vao trong {price: } va lay 2 gia tri thap phan
print(txt.format(price=49))

# cu phap.  string.format (value1, value2, value3,...)
# cac gia tri co the la bat ki kieu du lieu nao

# The placeholders: cac phan giu cho co the duoc xac dinh
# bang cach su dung cac chi muc duoc dat ten {price}, {0}, {}

# dinh dang gia tri fname, age va chen chung vao trinh giu cho
txt1= "My name is {fname}, I'am {age}".format(fname="John",age=36)

# chen gia tri vao trinh du cho
txt2= "My name is {0}, I'am {1}".format("John",36)
#chen gia tri vao trinh giu cho
txt3= "My name is {}, I'am {}".format("John",36)
print(txt1)
print(txt2)
print(txt3)

