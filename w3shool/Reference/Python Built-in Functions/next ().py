# ham next () tra ve phan tu tiep theo trong mot iterator : (trinh vong lap)

# tao doi tuong iterator
mylist = iter(["apple", "banana", "cherry"])

x=next(mylist,"vong lap ket thuc")
print(x)
x=next(mylist,"vong lap ket thuc")
print(x)
x=next(mylist,"vong lap ket thuc")
print(x)
x=next(mylist,"vong lap ket thuc")
print(x)

# cu phap next (iterable, default)
    #iterable: bat buoc , doi tuong iterable
    # default : khong bat buoc, gia tri tra ve neu vong lap ket thuc