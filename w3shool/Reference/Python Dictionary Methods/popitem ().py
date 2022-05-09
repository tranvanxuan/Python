# xoa cap gia tri duoc chen o cuoi cung

car={
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

# xoa cap gia tri o cuoi cung
car.popitem()

print(car)
# cu phap : dictionary.popitem (keyname, defaultvalue) : khong co tham so
# phan tu bi xoa tra ve gia tri la mot tuple.

x=car.popitem()
print(x)