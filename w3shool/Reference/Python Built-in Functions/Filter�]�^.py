# Loc mang va tra ve mang moi co gia tri >= 18

ages= [5, 12, 17, 18, 24, 32]

def myFunc(x):
    if x< 18:
        return False
    else:
        return True

adults = filter(myFunc, ages)

for x in adults:
    print(x)

# ham filter () tra ve gia tri, thong qua mot ham de kiem tra nhung gia tri day co duoc chap nhan hay khong
# filter (function, iterable)
