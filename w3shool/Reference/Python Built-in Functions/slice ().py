# ham slice tra ve mot doi tuong slice(cat)
# mot doi tuong lat

a=("a" , "b", "c", "d", "e", "f", "g", "h")
x=slice(2)
print(a[x])

# cu phap slice (start, end, step)
    # start: khong bat buoc, vi tri cat, mac dinh la 0
    # end : vi tri ket thuc
    # step : khong bat buoc, buoc nhay

b=("a" , "b", "c", "d", "e", "f", "g", "h")
y=slice(3,5)
print(a[y])

c=("a" , "b", "c", "d", "e", "f", "g", "h")
z=slice(0, 8, 3)
print(a[z])