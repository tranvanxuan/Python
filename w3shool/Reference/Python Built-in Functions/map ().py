# ham map () thuc thi mot ham duoc chi dinh cho tung phan tu trong mot lan lap. muc nay duoc gui den ham duoi dang tham so

# tinhdo dai moi tu trong mot vong lap
def myfunc(n):
    return len(n)

x=map(myfunc, ('apple', 'banana', 'cherry'))

for a in x:
    print(a)

# cu phap map (function, iterables)
    # funcion : bat buoc ham de thuc thi tung phan tu cua vong lap
    # iterable : mot chuoi, bo suu tap , hay doi tuong lap.
# Ban co the gui bao nhieu lan tuy thich , dam bao co mot tham so cho moi lan lap

def myfunc1(a,b):
    return (a +b)

y = map(myfunc1, ('apple', 'banana', 'cherry'), ('orange', 'lemon', 'pineapple'))

for z in  y:
    print(z)