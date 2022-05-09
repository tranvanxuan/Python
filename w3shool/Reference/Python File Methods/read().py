# tra ve noi dung cua file

# mo mot file de doc
f=open("demofile.txt", "r")
print(f.read())


# cu phap file.read (size)
    # size: khong bat buoc, so byte ban muon tra ve, mac dinh la -1 hien thi tat ca file

print("----------------------------------------------------------------------------\n")

# mo file de doc
f=open("demofile.txt", "r")

# doc 33 byte,(33 ki tu)
print(f.read(33))

