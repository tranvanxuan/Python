# ham open () mo mot file va tra ve doi tuong cua file do

f=open("demo.txt","r")
print(f.read())

# cu phap open (file, mode)
    # file : duong dan va ten cua file
    # mode : che do ban muon mo
        # r: doc , mo tep de doc, bao loi neu tep khong ton tai
        # a : noi them file
        # w : ghi vao file, tao file moi neu no khong ton tai
        # x : tao mot file, bao loi neu file ton tai
        # t: che do van ban
        # b : che do nhi phan, vi du hinh anh,...