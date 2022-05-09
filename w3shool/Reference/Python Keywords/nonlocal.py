# tu khoa nonlocal dung de lam viec voi bien ben trong cac ham long nhau
# su dung tu khoa none local de khai bao bien khong phai la cuc bo

# tao mot ham ben trong ham , cai ma dung bien x voi bien nonlocal
def myfunc1():
    x="John"
    def myfunc2():
        nonlocal x
        x="hello"
    myfunc2()
    return x

print(myfunc1())