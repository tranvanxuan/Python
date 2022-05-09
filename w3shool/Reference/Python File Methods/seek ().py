# phuong thuc seek () thay doi vi tri hien tai cua tep luong, tra ve vi tri moi


# mo file de doc
f=open("demofile.txt", "r")

# thay doi vi tri cua phan hien tai thanh 4 va tra ve phan con lai cua dong
f.seek(4)
print(f.seek(4))
print(f.readlines())

# cu phap f.seek(offset)
    # offset : bat buoc: mot so dai dien cho vi tri thay doi cua tep nguon

