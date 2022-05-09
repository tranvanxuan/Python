# tach chuoi khi ngat dong va tra ve danh sach

txt="Thank you for the music\nWelcome to the jungle"

x=txt.splitlines()
print(x)

# phuong thuc splitlines tach chuoi va tra ve danh sach, viec tach chuoi dien ra o noi ngat dong


# cu phap string.splitlines (kepplinebreaks) : keeplinebreaks giu lai ngat dong : True hoac False

txt="Thank you for the music\nWelcome to the jungle"

x=txt.splitlines(True)
print(x)
