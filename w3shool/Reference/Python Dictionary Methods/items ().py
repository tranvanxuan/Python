# tra ve mot danh sach tuple chua cap khoa-gia tri cua tu dien

car={
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
# tra ve mot danh sach moi phan  tu se chua cap khoa-gia tri cua tu dien
x=car.items()
print(x)

# cu phap dictionary.items () khong co tham so
car={
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

x=car.items()
car["year"]=2018

print(x)