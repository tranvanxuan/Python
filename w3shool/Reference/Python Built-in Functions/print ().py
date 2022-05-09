# ham print () in thong bao chi dinh ra man hinh.
# Thong bao co the la mot chuoi, hay bat ki doi tuong nao, doi tuong chuyen thanh chuoi truoc khi in ra man hinh

print("Hello World")

# cu phap print (object (s), separator = separator, end = end, file=file, flush=flush)
    # object bat ki doi tuong nao
    #separator: khong bat buoc chi cach tach doi tuong, neu co nhieu hon 1. mac dinh la ''
    #end : khong bat buoc chi dinh nhung gi se in o cuoi . mac dinh la \n
    #file : khong bat buoc, mot doi tuong voi mot phuong thuc viet, mac dinh la sys.stdout
    # flush khong bat buoc. mot boolean, chi dinh dau ra dung hoac sai, mac dinh la False

# In nhieu hon mot doi tuong

print("hello", "how are you?")

x= ("apple", "banana", "cherry")

print(x)

print("Hello", "how are you?", sep="---",end='\n',)