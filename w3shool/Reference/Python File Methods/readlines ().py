# tra ve mot danh sach chua moi dong trong tep.
# su dung tham so hint de gioi han so luong dong tra ve

# mo file de doc
f=open("demofile.txt", "r")

# tra ve tat ca cac dong trong tep duoi dang danh sach
print(f.readlines())

#  cu phap  file.readlines(hint)
    # khong bat buoc. so byte ban muon tra ve, mac dinh la -1. tra ve tat ca cac dong
    # khong tra ve dong tiep theo neu lon hon so byte ban muon tra ve

print("-------------------------------------------------------")
f=open("demofile.txt", "r")
print(f.readlines(5))

