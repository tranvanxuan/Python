# phuong thuc partition () tra ve mot chuoi trong do chuoi chia thanh 3 phan

txt="I could eat bananas all day"

# tim tu bananas va tra ve vong lap gom 3 phan tu
x=txt.partition("bananas")
print(x)

# cu phap string.partition (value)  value : chuoi se duoc tim kiem
### chu y phuoc thuc nay tim kiem lan xuat hien dau tien cua chuoi

txt=" I could eat bananas all day"

# neu khong tim thay gia tri, se tra ve tuple
# phan tu 1 : chuoi ban dau
# phan tu 2 rong
# phan tu 3 rong
x=txt.partition("apple")
print(x)