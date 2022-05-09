# tra ve mot tu dien voi tu khoa va gia tri duoc chi dinh

# tao tu dien voi 3 tu khoa, va tat ca gia tri 0
x={'key1', 'key2', 'key3'}
y=0

thisdict=dict.fromkeys(x, y)

print(thisdict)

# cu phap dict.fromkeys (keys, value)
    # keys : can thiet, vong lap chi dinh khoa cua tu dien moi
    # values: khong bat buoc. gia tri cua tat ca cac khoa, gia tri mac dinh la None

# tao tu dien voi 3 khoa, va gia tri none
x=('key1', 'key2', 'key3')
thisdict=dict.fromkeys(x)
print(thisdict)