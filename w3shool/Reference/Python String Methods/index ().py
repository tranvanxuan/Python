# phuong thuc index () tim trong chuoi mot gia tri cua the va tra ve vi tri neu duoc tim thay
txt= "Hello, welcome to my world."
# tra ve vi tri cua welcome neu duoc tim thay
x=txt.index("welcome")
print(x)

# ham phuong thuc index () tra ve ngoai le neu khong tim thay gia tri

# cu phap string.index(value, start, end)

txt="Hello, welcome to my world."

#tra ve vi tri cua "e" neu duoc tim thay
x=txt.index("e")
print(x)

txt="Hello, welcome to my world."
#tra ve vi tri cua "e" giua vi tri 5 va 10 neu duoc tim thay
x=txt.index("e", 5, 10)
print(x)

txt="Hello, welcome to my world."
print(txt.index("q"))
print(txt.index("p"))
