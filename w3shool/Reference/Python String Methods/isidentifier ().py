# phuong thuc isidentifer ()  tra ve True neu chuoi la mot dinh danh hop le nguoc lai tra ve False
# mot chuoi duoc coi la mot dinh danh hop le neu chua cac chu (a-z) va so (0-9) hoac dau gach duoi (_)
# dinh dang hop le khong bat dau bang so hoac chua bat ki khoang trang nao


txt="Demo"
x=txt.isidentifier()
print(x)

# cu phap string.isidentifier () khong co tham so
a="MyFolder"
b="Demo002"
c="2bring"
d="my demo"

print(a.isidentifier())
print(b.isidentifier())
print(c.isidentifier())
print(c.isidentifier())