# Ham all()  tra ve true neu tat cac cac gia tri trong mot lan lam la true
#neu khong no se tra ve Fails
# Neu doi tuong lap lai - Iterable trong ham all tra ve True

###Cu phap all(doi tuong lap) : doi tuong lap co the la (list,tuple,dictionary)

# doi tuong lap la danh sach
mylist=[0,1,1]

# ham all
x = all(mylist)

print(x)

# doi tuong lap la tuple
mytuple=(0, True, False)

y=all(mytuple)

print(y)

# Doi tuong lap la mot bo gia tri
myset={0,1,0}

z=all(myset)

print(z)

# Doi tuong lap la mot bo tu dien
mydict={0: "Apple", 1: "Orange"}

w=all(mydict)
print(w)