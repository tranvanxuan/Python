# Phuong thuc isumeric () tra ve true neu tat ca ki tu la so (0-9), nguoc lai False
# so mu nhu ^2 va 3/4 la mot gia tri so

txt="575543"

# kiem tra xem cac ki tu trong chuoi txt co phai la so khong
x=txt.isnumeric()
print(x)

# cu phap string.isnumeric () . Khong co tham so

a="\u0030" # unicode for 0
b="\u00B2" # unicode for &sup2
c="10km2"
print(a.isnumeric())
print(b.isnumeric())
print(c.isnumeric())

