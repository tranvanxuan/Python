# phuong thuc shuffle () lay mot chuoi (danh sach, chuoi, tuple)  va sap xep lai thu tu cac muc
import  random
mylist = ["apple", "banana", "cherry"]
random.shuffle(mylist)
print(mylist)


# cu phap  random..shuffle (sequence, function)
    #  sequence : bat buoc:  chuoi, danh sach, tuple
    # ten cua ham tra ve mot so trong khoang tu 0,0 den 1, neu khong duoc chi dinh , ham random () se duoc su dung


    # ban co the khai bao  cac ham de can nhac hoac chi dinh ket qua
    # neu ham tra ve cung mot so moi lan, ket qua se theo cung mot thu tu moi lan

# khai bao ham myfunction () va tra ve 0.1
def myfunction ():
    return 0.1

# khai bao list
mylist = ["apple", "banana", "cherry"]


random.shuffle(mylist, myfunction)

print(mylist)