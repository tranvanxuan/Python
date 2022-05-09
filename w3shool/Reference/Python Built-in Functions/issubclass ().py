# Ham issubclass () tra ve true neu doi tuong duoc chi dinh la lop con cua doi tuong duoc chi dinh, neu khong la False
class myAge:
    age=36

class myObj(myAge):
    name="John"
    age=myAge

x=issubclass(myObj,myAge)

print(x)

# cu phap issubclass (object, subclass)
    # object : bat buoc, doi tuong
    # subclass: mot doi tuong lop hoac mot bo cua doi tuong lop