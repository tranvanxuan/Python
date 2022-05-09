# Ham delattr () se xoa mot thuoc tinh cu the tu mot doi tuong cu the

class Persion:
    name="John"
    age="36"
    country="Norway"

delattr(Persion,'age')

x=Persion()

print(x.name)

print(x.age) # bao loi la thuoc tinh age da bi xoa 