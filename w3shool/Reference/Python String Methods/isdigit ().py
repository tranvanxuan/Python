# phuong thuc isdigit () tra ve  "TRUE" neu tat ca ki tu la so, nguoc lai False
# so mu la so

txt="50800"
# kiem tra tat ca ki tu co phai la so
x=txt.isdigit()
print(x)

# cu phap isdigit () khong co tham so

a="\u00030" # unicode for 0
b="\u00B2" #unicode for ^2

print(a.isdigit())
print(b.isdigit())