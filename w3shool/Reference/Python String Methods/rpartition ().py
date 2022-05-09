# tra ve mot tuple trong do chuoi chia thanh 3 phan


txt="I could eat bananas all day, bananas aremy favorite fruit"

# tim lan xuat hien cuoi cung cua tu "bananas" va tra ve chuoi gom 3 phan
x=txt.rpartition("bananas")
print(x)

# cu phap string.rpartition (value) : value 'gia tri can tim'

# neu chuoi khong duoc tim thay
    # phan tu 1 : rong
    #phan tu 2 : rong
    # phan tu 3 : la ban than chuoi
txt="I could eat bananas all day, bananas aremy favorite fruit"
print(txt.rpartition("apples"))