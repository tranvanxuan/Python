# xoa bo phan tu o trong tap hop nay va khong co trong cac bo duoc chi dinh khac

x={"apple", "banana", "cherry"}
y= {"google", "microsoft", "apple"}

x.intersection_update(y)
print(x)

# phuong thuc intersection_update () loai bo cac phan tu khong xuat hien trong 2 hay nhieu bo.
# phuong thuc intersection_update () khac phuong thuc intersection ().
# boi vi intersection () tra ve mot bo moi, khong bao gom phan tu khong mong muon
# intersection_update () loai bo phan tu khong mong muon trong bo ban dau

# cu phap set.intersection_update (set1, set2, ...etc)
    # set1 : bat buoc tap hop de tim kiem cac muc giong nhau
    # set2 : khong bat buoc. tap hop khac de tim kiem, ban co the so sanh nhieu bo neu ban muon, ngan cach nhau bang dau ,

x={"a", "b", "c"}
y={"c", "d", "e"}
z={"f", "g", "c"}

x.intersection_update(y,z)
print(x)
