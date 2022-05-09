# Ham any() tra ve true neu  mot trong cac phan tu la True
# Faile neu khong tra ve False
 # neu doi tuong vong lap dung tra ve fails

# doi tuong lap la tuple

mytuple=(0,1, False)
x = any(mytuple)

print(x)

# doi tuong lap la mot tap gia tri
myset = {0,1,0}

y=any(myset)

print(y)

# doi tuong lap la mot bo tu dien
mydict = {0 : "Apple", 1: "Orange"}

z=any(mydict)

print(z)