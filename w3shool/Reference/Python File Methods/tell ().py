# tra ve vi tri cua tep hien tai trong mot tep luong

# mo file de doc
f=open("demofile.txt", "r")
# tra ve vi tri hien tai cua tep trong tep luong
print(f.tell())

# cu phap file.tell ()

# mo file de doc
f=open("demofile.txt", "r")

print(f.readlines())
# tra ve vi tri tep hien tai sau khi dong dong dau tien
print(f.tell())