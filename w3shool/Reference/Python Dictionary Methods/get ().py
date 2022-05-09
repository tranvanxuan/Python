# tra ve gia tri cua khoa chi dinh

# lay gia tri cua phan tu "model"

car={
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

# lay gia tri cua khoa "model"
x=car.get("model")
print(x)

# cu phap dictionary.get (keyname, value)
    # key_name : can thiet: ten tu khoa cua phan tu ban muon lay gia tri tu
    # value : khong bat buoc. 1 gia tri tra ve neu khoa chi dinh khong tim thay, mac dinh la None

car = {
    "brand": "Ford",
    "model": "Mustang",
    "Year": 1964
}

x=car.get("price", 15000)
print(x)