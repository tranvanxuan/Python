# phuong thuc sort () sap xep danh sach

cars=['Ford', 'BMW', "Volvo"]

# sap xep danh sach theo chu
cars.sort()
print(cars)

# cu phap list.sort(reverse= True|False, key=myFunc)
    # reverse :khong bat buoc, dao nguoc, True : sap xep giam dan, mac dinh la False
    #key  : khong bat buoc, mot ham de xac dinh cac tieu chi sap xep

cars=['Ford', 'BMW', "Volvo"]

# sap xep giam dan
cars.sort(reverse=True)
print(cars)

# mot ham tra ve do dai cua ki tu
def myFunc (e):
    return len(e)

cars=['Ford','Mitsubishi', 'BMW', "VW"]

# sap  xep danh sach theo do dai ki tu
cars.sort(key=myFunc)
print(cars)
