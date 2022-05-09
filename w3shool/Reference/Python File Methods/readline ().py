# tra ve mot dong dau tien tu mot tep
# ban co the chi dinh bao nhieu bytes tu tep tra ve , bang cach dung tham so size

# mo file de doc
f=open("demofile.txt", "r")

# tra ve dong dau tien cua tep
print(f.readline())

# cu phap file.readline(size)
    # size : khong bat buoc: so byte  ban muon tra ve, mac dinh la -1 . hien thi tat ca

f=open("demofile.txt", "r")
print(f.readline(2))
print(f.readline(10))
f.close()