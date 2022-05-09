# phuong thuc expandtabs () dat kic thuoc tab bang so luong khoang trang da duoc chi dinh.
txt="H\te\tl\tl\to"

# \t tab , dat ki thuco tab bang 2 ki tu trang
x=txt.expandtabs(2)
print(x)

txt="H\te\tl\tl\to"
print(txt)
print(txt.expandtabs())
print(txt.expandtabs(2))
print(txt.expandtabs(4))
print(txt.expandtabs(10))

# cu phap string.expandtabs(tabsize)