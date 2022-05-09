# tra ve mot tap hop chua su khac nhau giua 2 hay nhieu tap hop
# nghia la tra ve tap hop gom phan tu ton tai duy nhat trong tap hop dau tien
# va khong ton tai trong ca hai

x={"apple", "banana", "cherry"}
y={"google", "microsoft", "apple"}

# tra ve tap hop phan tu chi ton tai trong tap hop x ma khong ton tai trong tap y
z=x.difference(y)

print(z)

# cu phap set.difference(set)
# tham so set : bat buoc: tap hop de so sanh su khac nhau

x={"apple", "banana", "cherry"}
y={"google", "microsoft", "apple"}

z=y.difference(x)
print(z)