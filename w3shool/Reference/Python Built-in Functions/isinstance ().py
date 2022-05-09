# ham isinstance () tra ve True neu doi tuong chi dinh thuoc loai da duoc chi dinh. Ngoai ra tra ve False
# Neu doi tuong la mot tuple, ham nay se tra ve True neu doi tuong la mot trong cac loai trong bo
# kiem tra xem 5 co thuoc kieu nguyen khong
x=isinstance(5, int)
print(x)

y=isinstance("Hello",(float,int,str,list,dict,tuple))

print(y)

class myObj:
    name="John"
z = myObj()

w=isinstance(z,myObj)
print(w)