
mylist = ['apple', 'banana', 'cherry']
# Dong ban danh sach va lam cho no khong the thay doi
x=frozenset(mylist)

# Ham frozenset tra ve doi tuong frozenset.( Giong doi tuong duoc dat, chi duy nhat khong the thay doi)
#  cu phap frozenset (iterable)
# iterablle : doi tuong lap giong nhu list,set, tuple, ...

# Neu ban co thay doi gia tri cua mot phan tu frozenset , Se bao loi
x[1]= "strawberry"

