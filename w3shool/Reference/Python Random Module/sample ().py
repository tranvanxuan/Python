import random

mylist= ["apple", "banana", "cherry"]

# tra ve mot danh sach chua 2 phan tu trong so cac phan tu tu danh sach
print(random.sample(mylist, k=2))

# phuong thuc nay khong thay doi trinh tu ban dau

# cu phap random.sample (sequence, k)
    # sepuence can thiet: list, set, range, etc
    # k : can thiet: kich thuoc cua danh sach tra ve