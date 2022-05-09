import random

mylist=["apple", "banana", "cherry"]
# tra ve mot danh sach voi 14 phan tu
# danh sach nen chua mot lua chon ngau nhien  cac gia tri tu mot danh sach duoc chi dinh va kha nang chon tao cao hon 10 lan so voi gia tri con lai
print(random.choices(mylist, weights=[10, 1, 1], k= 14))

# cu phap  random.choices (sequence, weights = None, cum_weights = None, K=1)
    # sequence : chuoi, danh sach, tuple, etc
    # weithts mot danh sach ban co the can nhac kha nang cho tung gia tri
    # K khong bat buoc, mot so nguyen khai bao do dai cua chuoi tra ve