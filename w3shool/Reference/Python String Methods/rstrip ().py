txt="    banana    "

# xoa khoang trang ben phai chuoi banana
x=txt.rstrip()
print("of all fruits", x, "is my favorite")

# phuong thuc rstrip () xoa bat ki ki tu dau ben phai chuoi. mac dinh la ki tu trang

# cu phap string.rstrip(characters)
    # characters : ki tu dau, khong bat buoc

txt="banana,,,,,ssaaww....."

# xoa bo bat ki ki tu ",.asw" ket thuc chuoi
x=txt.rstrip(",.asw")

print(x)