#  thay the gia tri chi dinh thanh mot gia tri duoc chi dinh

txt="I like bananas"

# thay the tu bananas thanh apples
x=txt.replace("bananas", "apples")

print(x)

# cu phap string.replace (oldvalue, newvalue, count) count : so lan thay the cac gia tri cu, mac dinh la tat ca

txt= "one one was a race horse, two two was one too."
# thay the tu one thanh tu three 2 lan
x=txt.replace("one", "three", 2)

print(x)