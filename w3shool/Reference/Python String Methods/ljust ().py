txt="banana"

# tra ve mot ki tu dai 20 ki tu, ben trai ket qua la tu "banana"
# trong ket qua co 14 ki tu trang ben phai tu "banana"
x=txt.ljust(20)
print(x,"is my favorite fruit.")

# phuong thuc ljust () can le ben tra mot chuoi, dung ki tu chi dinh (mac dinh la cach) lam ki tu ngan cach

# cu phap string.ljust (length, character)
    # length : bat buoc, do dai chuoi tra ve
    # khong bat buoc: ki tu ngan cach, mac dinh la " " (cach)

txt="banana"

x=txt.ljust(20,"0")
print(x)