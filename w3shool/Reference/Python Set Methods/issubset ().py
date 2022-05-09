# tra ve True neu tat ca phan tu ton tai trong mot bo chi dinh, nguoc lai tra False

x={"a", "b", "c"}
y={"f", "e", "d", "c", "b", "a"}

# kiem tra xem tat ca phan tu trong x co nam trong y
z=x.issubset(y)
print(z)

# cu phap set.issubset (set)

x={"a", "b", "c"}
y={"f", "e", "d", "c", "b"}

z=x.issubset(y)
print(z)