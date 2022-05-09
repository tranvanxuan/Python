# Phuong thuc encode () ma hoa chuoi theo phuong thuc chi dinh,. Neu khong co phuong thuc nao chi dinh, UTF-8 se duoc dung
txt = "My name is Stale"
# ma hoa chuoi theo phuong thuc UTF-8
x = txt.encode()
print(x)

# Cu phap string.encode (encoding=encoding, error=errors)
# encoding: khong bat buoc, phuong thuc ma hoa. Neu khong co phuong thuc nao duoc dung. mac dinh la UTF-8
# Errors : mot chuoi xac dinh phuong thuc loi.Gia tri hop phap la
# ' backslashreplace' : su dung ki tu gach cheo thay neu khong the ma hoa
# 'ignore' : bo qua ki tu khong the ma hoa
# 'namereplace' : thay the ki tu voi mot doan van ban
# 'strict'
# 'replace' : thay the ki tu voi dau ?
# 'xmlcharrefreplace' : thay the ki thu voi ki tu xml

txt = "My name is Stale"

print(txt.encode(encoding="ascii", errors="backslashreplace"))
print(txt.encode(encoding="ascii", errors="ignore"))
print(txt.encode(encoding="ascii", errors="namereplace"))
print(txt.encode(encoding="ascii", errors="replace"))
print(txt.encode(encoding="ascii", errors="xmlcharrefreplace"))
print(txt.encode(encoding="ascii", errors="strict"))
