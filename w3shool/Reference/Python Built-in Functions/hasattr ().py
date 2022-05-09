# ham hasattr () tra ve True  neu mot doi tuong duoc chi dinh, co thuoc tinh chi dinh. Ngoai ra tra ve False

class Person:
    name = "John"
    age="36"
    country="Norway"

# kiem tra xem doi tuong Person co thuoc tinh tuoi khong
x=hasattr(Person,'age')

print(x)

# cu phap hasattr (object, attribute)