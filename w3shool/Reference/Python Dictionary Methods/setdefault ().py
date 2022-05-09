# tra ve gia tri cua tu khoa duoc chi dinh. neu tu khong khong ton tai, them tu khoa voi gia tri chi dinh

car= {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

x=car.setdefault("model", "Bronco")
print(x)

# cu phap dictionary.sedefault (keyname, value)
    # keyname : can thiet, tu khoa cua phan tu ban muon tra ve
    # value : khong bat buoc, neu tu khoa ton tai, tham so khong co tac dung
                              # neu khoa khong ton tai tham so se tra thanh gia tri cua khoa, mac dinh la "None"

x=car.setdefault("coler", "white")
print(x)
