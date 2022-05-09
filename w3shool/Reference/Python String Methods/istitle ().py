# phuong thuc istitle () tra ve True neu tat cac
# cac tu trong van ban bat dau bang chu in hoa
#va phan con lai cua tu la chu thuong. nguoc lai False

txt="Hello, And Welcome To My World!"

# kiem tra xem moi tu bat dau bang mot chu cai viet thuong
x=txt.istitle()
print(x)

# cu phap string.istitle () khong co tham so

a="HELLO, AND WELCOME TO MY WOLD" # false
b="Hello" #true
c="22 Names" # true
d="This Is %'!?" # True

print(a.istitle())
print(b.istitle())
print(c.istitle())
print(d.istitle())