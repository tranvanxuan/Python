# ham memoryview () tra mot doi tuong xem bo nho tu mot doi tuong duoc chi dinh

# tra ve doi tuong xem bo nho
x=memoryview(b'Hello')
print(x)

y=memoryview(b'\x00\x00\x00')
print(y)

# cu phap memoryview (obj) obj: doi tuong byte hoac doi tuong bytearray