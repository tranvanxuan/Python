# tra ve danh sach tat ca gia tri cua tu dien

car={
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

# tra ve danh sach tat ca gia tri cua tu dien
x=car.values()
print(x)

# cu phap dictionary.values ()

car={
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

# khi gia tri bi thay doi trong tu dien, doi tuong se duoc cap nhat
x = car.values()
car["year"]=2018

print(x)