# ham setattr () dat gia tri cua thuoc tinh duoc chi dinh cua doi tuong duoc chi dinh

class Person:
    name="John"
    age = 36
    country= "Norway"

setattr(Person,'age',40)

x=getattr(Person, 'age')
print(x)

# cu phap setattr (object, attribute, value)