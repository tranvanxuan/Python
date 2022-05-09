# tra ve true neu khong co muc nao ton tai o ca 2 tap hop, nguoc lai tra ve False

x={"apple", "banana", "cherry"}
y={"google", "microsoft", "facebook"}

z=x.isdisjoint(y)

print(z)

# cu phap set.isdisjoint (set)
    # set can thiet. tap hop de tim kiem

x={"apple", "banana", "cherry"}
y={"google", "microsoft", "apple"}

z=x.isdisjoint(y)
print(z)