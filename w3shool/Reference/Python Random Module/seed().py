# Python co mot modul tich hop ma ban co the su dung de tao cac so ngau nhien
# modul ngau nhien co mot bo phuong thuc
# khoi tao trinh tao so ngau nhien

import random

# dat gia tri la 10 va xem dieu gi xay ra
random.seed(10)
print(random.random())

# trinh tao so ngau nhien can mot so de bat dau bang, de co the tao mot so ngau nhien
#Theo mac dinh, trinh tao so ngau nhien su dung thoi gian he thong hien tai
#Su dung phuong thuc seed () de tuy chinh so bat dau cua trinh tao so ngau nhien
# neu ban su dung cung mot gia tri hat giong 2 lan, ban se nhan duoc cung mot so ngau nhien 2 lan

# cu phap random.seed (a, version)
    # khong bat buoc, gia tri de tao ra so ngau nhien,
    # neu la so nguyen duoc su dung truc tiep,neu khong no phai duoc chuyen doi thanh so nguyen
    #gia tri mac dinh la khong va neu khong trinh tao su dung thoi gian he thong hien tai

# Mot so nguyen chi dinh cach chuyen doi tham so thanh so nguyen. gia tri mac dinh la

# neu ban su dung cung mot gia tri hat giong 2 lan, ban se nhan duoc cung mot so ngau nhien 2 lan

random.seed(9)
print(random.random())

random.seed(9)
print(random.random())