x={"apple", "banana", "cherry"}
y={"google", "microsoft", "apple"}

# xoa bo phan tu trong tap hop x ton tai tren cai 2 tap hop
x.difference_update(y)
print(x)

# phuong thuc difference_update () loai bo phan tu ton tai tren 2 tap hop
# phuong thuc difference_update () khac phuong thuc
# boi vi phuong thuc difference () tra ve mot tap hop moi, khong co phan tu khong mong muon
# phuong thuc difference_update () xoa bo phan tu khong muong muon

# cu phap set.difference_update (set)
    # set : can thiet. tap hop kiem tra su khac nhau