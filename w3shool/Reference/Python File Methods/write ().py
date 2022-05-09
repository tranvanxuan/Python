# ghi chuoi chi dinh len tep hien tai
# truong hop van ban duoc chi dinh se duoc chen tuy thuoc vao che do tep va vi tri luong
    # a : van ban se duoc chen tai vi tri luong tep hien tai, mac dinh o cuoi tep
    # w : tep se bi xoa truoc khi van ban duoc chen vao, mac dinh la 0

# mo file de them vao cuoi file
f=open("demofile1.txt", "a")

# chi chuoi vao vi tri cuoi file
f.write("See you soon!")
# dong file
f.close()

# mo file de doc
f=open("demofile1.txt", "r")
print(f.read())

# cu phap file.write (byte) : byte : van ban hay doi tuong byte se chen vao

f=open("demofile1.txt", "w")
f.write("See you soon!")
f=open("demofile1.txt", "r")
f.read()