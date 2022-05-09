# ham vars () tra ve thuoc tinh __dic__ cua mot doi tuong
# thuoc tinh __dic__ la mot  tu dien chua cac thuoc tinh co the thay doi cua doi tuong
# goi ham vars () khong co tham so se tra ve mot tu dien co chua bang ki hieu cuc bo

class Person:
    name="John"
    age=36
    country= "norway"

# tra ve thuoc tinh __dic__ cua doi tuong.
x=vars(Person)

print(x)

# cu phap vars(object)
    #object: bat ki doi tuong nao co chua thuoc tinh __dict__
print(vars())