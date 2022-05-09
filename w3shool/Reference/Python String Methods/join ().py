myTuple = ("John", "Peter", "Vicky")

# noi tat ca cac phan tu trong mot danh sach , dung ki tu # de ngan cach
x="#".join(myTuple)
print(x)

# phuong thuc join () noi tat ca phan tu trong 1 lan lap thanh mot chuoi
# Mot chuoi phai duoc chi dinh lam dau phan cach
# cu phap. string.join (iterable)
# iterable : bat ki doi tuong lap nao

myDict = {"name": "John", "country": "Norway"}
mySeparator = "TEST"

# noi tat ca phan tu trong tu dien thanh mot chuoi, dung tu TEST lam dau phan cach
x=mySeparator.join(myDict)
print(x)

# khi ban dung tu dien la vong lap, gia tri tra ve la tu khoa, khong phai gia tri cua vong lap