# phuong thuc strip () cat chuoi

txt= "    banana    "
x=txt.strip()
print(x)

# cu phap string.strip (characters)
# ki tu cat

txt= ",,,,rrttgg.....banana....rrr"

# loai bo ki tu ,.grt trong chuoi
x=txt.strip(",.grt")

print(x)