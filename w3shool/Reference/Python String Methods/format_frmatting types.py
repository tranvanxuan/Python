# Ben trong cac trinh giu cho , ban co the them mot loai dinh dang de dinh dang ket qua

#  can trai va dat khong gian co san la 8 ki tu "49       " khong gian la 8 , dem tu 0-  can trai 7 ki tu cach
txt="We have {:<8} chickens."
print(txt.format(49))

# can phai va dat khong gian co san la 8 ki tu
txt="We have {:>8} chickens."
print(txt.format(49))

# can phai 7 ki tu
txt="We have {:^8} chickens."
print(txt.format(49))