import re

txt = "8 times + before + 11:45 AM"

x = re.findall("aix*", txt)
print(x)
print(re.findall("[+]", txt))

