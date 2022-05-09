# ham sorted () tra ve mot danh sach da duoc sap xep.
# co the chi dinh sap xep tang dan hoac giam dan, chuoi sap xep theo abc, va so sap xep theo so
# ban khong the sap sap 1 chuoi co ca so va chuoi

a=("b", "g", "a", "d", "f", "c", "h", "e")
# sap xep a theo thu tu tang dan
x=sorted(a)
print(x)

# cu phap sorted (iterable, key=key, reverse=reverse)
    # iterable , bat buoc,doi tuong lap
    #key : khong bat buoc, mac dinh la khong
    # reverse: khong bat buoc, kieu boolean, False : sap xep tang dan, Rrue sap xep giam dan, mac dinh la False

a=("b", "g", "a", "d", "f", "c", "h", "e")
x=sorted(a,reverse=True)
print(x)