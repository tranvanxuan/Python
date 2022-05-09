# tra ve mot tap hop la giao cua 2 tap hop khac nhau

x={"apple", "banana", "cherry"}
y={"google", "microsoft", "apple"}

# tap hop z la giao cua 2 tap hop x va y
z=x.intersection(y)

print(z)

# cu phap set.intersection (set1, set2,...etc)
    # set1 : bat buoc
    # set2 : khong bat buoc,tap hop khac de tim kiem muc giong nhau.
            # ban co the so sanh bao nhieu bo neu ban thich. cac bo ngan cach nhau boi dau ,

x={"a", "b", "c"}
y={"c", "d", "e"}
z={"f", "g", "c"}

result= x.intersection(y, z)
print(result)