# ham inter () tra ve doi tong iterator
# cu phap iter (object, sentinel)
    # object : bat buoc, doi tuong iterable
    #sentinel: khong bat buoc, neu doi tuong la mot doi tuong co the goi duoc ,
# viec lap se dung lai khi gia tri duoc tra ve giong nhu gia tri

x=iter(["apple", "banana", "cherry"])

print(next(x))
print(next(x))
print(next(x))
# bao loi dong 12 vi doi tuong tra ve bi trung
print(next(x))