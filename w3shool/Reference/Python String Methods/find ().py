# phuong thuc find () tim trong chuoi mot gia tri c the va tra ve vi tri neu gia tri duoc tim thay

txt="Hello, welcome to my world."

# tra ve vi tri chuoi "welcome" trong chuoi txt neu duoc tim thay
x=txt.find("welcome")

print(x)

# cu phap string.find (value, start, end)
# phuong thuc find () tra ve -1 neu gia tri khong tim thay
# phuong thuc find () gan giong voi phuong thuc index(),
# diem khac biet duy nhat la phouong thuc index dua ra truong hop ngoai le neu gia tri khong tim thay


txt="Hello, welcome to my world."
# tra ve vi tri gia tri "e" neu duoc tim thay
x=txt.find("e")
print(x)

txt="Hello, welcome to my world."
# tra ve vi tri e bat dau tu vi tri 5 den vi tri 10
x=txt.find("e", 5, 10)
print(x)


txt="Hello, welcome to my world."
print(txt.find("q"))
print(txt.find("p"))