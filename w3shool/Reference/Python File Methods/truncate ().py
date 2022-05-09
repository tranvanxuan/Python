# thay doi kich thuoc tep thanh so byte  da cho
# neu kich thuoc khong duoc chi dinh, vi tri hien tai se duoc su dung
# mo file de noi them phan tu moi
f=open("demofile1", "a")

# thay doi kich thuoc tep
f.truncate(20)
f.close()

# mo file de doc
f=open("demofile1.txt", "r")

print(f.read())

# cu phap file.truncate (size)
    # size : khong bat buoc, kich thuoc cua tep sau khi cat ngan