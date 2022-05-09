# xoa phan tu voi khoa chi dinh

car= {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

car.pop("model")
print(car)

# cu phap dictionary.pop (keyname, defaultvalue)
    # keyname : can thiet, khoa cua phan tu ban muon xoa
    # defaultvalue: khong bat buoc. gia tri tra ve neu khoa chi dinh khong tim thay. neu khong co se tra ve loi ngoai le

car={
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

x=car.pop("color","khong tim thay gia tri")
print(x)