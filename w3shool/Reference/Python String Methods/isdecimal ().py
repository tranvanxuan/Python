# phuong thuc isdecimal () tra ve True neu tat cac cac ki tu la so thap phan (0-9)
# puong thuc nay dung doi tuong unicode

txt="\u0033" # unicode for 3
x=txt.isdecimal()
print(x)

# cu phap string.isdecimal () : khong co tham so

# kiem tra neu tat ca ki tu la ki tu unicode so thap phan
a="\u0030" # unicode for 0
b="\u0047" # unicode for G

print(a.isdecimal())
print(b.isdecimal())