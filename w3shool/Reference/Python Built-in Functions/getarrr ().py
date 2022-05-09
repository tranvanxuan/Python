# Ham getattr () tra ve gia tri cua the cua mot thuoc tinh cu the tu doi tuong cu the

class Person:
    name="John"
    age="36"
    country="Norway"

# tra ve gia tri cua thuoc tinh tuoi tu doi tuong Person
x=getattr(Person,'age')

# in ra man hinh
print(x)

# Cu phap getattr (object, attribute,default)
    #object: bat buoc, doi tuong
    # attribut : Ten cua thuoc tinh ban muon lay gia tri
    # defaut: khong bat buoc, gia tri tra ve neu thuoc tinh do khong ton tai

y=getattr(Person,'page',"Thuoc tinh khong ton tai")

print(y)