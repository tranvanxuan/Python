# tra ve mot phien ban cat ben trai cua chuoi

txt="    banana    "

x=txt.lstrip()

print("of all fruits", x, "is my favorite")

# cu phap  string.lstrip (characters)
 # characters: khong bat buoc, ki tu se bi cat

txt=",,,,ssaaww.....banana"

# cat ki tu ",.asw" ben trai trong chuoi
x=txt.lstrip(",.asw")

print(x)