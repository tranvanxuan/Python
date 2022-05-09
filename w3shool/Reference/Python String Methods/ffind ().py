# tim kiem trong chuoi mot gia tri cu the va tra ve vi tri xuat hien cuoi neu duoc tim thay

txt="Mi casa, su casa."

# tra ve vi tri xuat hien cuoi cung cua  tu casa
x=txt.rfind("casa")

print(x)

# cu phap string.frind(value, start, end)
# phuong thuc se tra ve -1 neu khong tim thay

txt="Hello, welcome to my world."

# tra ve vi tri lan cuoi xuat hien cua tu e , tim kiem tu 5 den 10
x=txt.rfind("e", 5, 10)

print(x)

txt="Hello, welcome to my world."
print(txt.rfind("q"))
