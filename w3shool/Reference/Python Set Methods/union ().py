# neu 2 bo voi nhau
x={"apple", "banana", "cherry"}

y={"google", "microsoft", "apple"}

# noi 2 bo voi nhau, phan tu trung lap bi loai bo
z=x.union(y)
print(z)

# cu phap set.union (se1, set2,...)
    #set1: can thiet bo de hop nhat voi
    #set2: khong bat buoc, bo khac de hop nhat voi
        #ban co the them bao nhieu bo tuy thich, cac bo ngan cach voi nhau bang dau phay

x={"a", "b", "c"}
y={"f", "d", "a"}
z={"c", "d", "e"}

result= x.union(y,z)
print(result)