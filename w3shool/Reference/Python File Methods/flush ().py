# lam sach bo dem ben trong

# mo file
f=open("demofile.txt", "a")

# ghi tiep vao cuoi file
f.write("Now the file has one more line!")
# xoa bo nho dem sau khi ghi vao tep
f.flush()
# ghi vao cuoi file
f.write("...and another one")

# cu phap file.fileno ()