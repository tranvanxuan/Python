# ghi mot danh sach chuoi vao tep

# mo file che do "a" de noi them vao file
f=open("demofile3.txt", "a")
# ghi danh sach vao chuoi
f.writelines(["See you soon!", "Over and out."])

# dong file
f.close()

# mo file de doc
f=open("demofile3.txt", "r")
print(f.read())