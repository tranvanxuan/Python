txt="apple, banana, cherry"

#chia mot chuoi thanh danh sach, dung (, ) lam ki tu ngan cach
x=txt.rsplit(", ")
print(x)

# phuong thuc rsplit () chia mot chuoi thanh mot danh sach, bat dau tu ben phai
# neu khong co "max" duoc chi dinh, se tra ve ket qua giong phuong thuc split
# khi max duoc chi dinh, danh sach se chua so phan tu + 1


# cu phap string.rsplit (separator, max)
    #separator : khong bat buoc, ki tu ngan cach mac dinh l ''
    # max : khong bat buoc, bao nhieu lan ngan cach. mac dinh la -1 (tat ca cac lan xuat hien)

txt="apple, banana, cherry"
# chia mot chuoi thanh danh sach toi da 2 phan tu
x=txt.rsplit(", ", 1)
print(x)