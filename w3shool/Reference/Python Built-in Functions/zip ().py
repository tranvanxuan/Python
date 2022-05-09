# ham zip () tra ve mot doi tuong zip. la mot trinh lap cua cac bo dulieu ,
# trong do muc dau tien cua cac vong lap duoc noi voi nhau
# va sau do muc thu 2 cua cac vong lap duoc noi voi nhau,...
# neu cac trinh vong lap co do dai khac nhau, thi trinh vong lap co it muc nhat se quyet dinh do dai cua trinh vong lap moi
a= ("John", "Charles", "Mike")
b=("Jenny", "Christy", "Monica")
# tra ve doi tuong zip()
x=zip(a,b)
# su dung ham tuple de hien thi phien ban co the doc duoc cua ket qua
print(tuple(x))

# tao vong lap a va b
a= ("John", "Charles", "Mike")
b=("Jenny", "Christy", "Monica", "Vicky")
# tao doi tuong zip
x=zip(a,b)
# su dung ham tuple de hien thi phien ban co the doc duoc cua ket qua
print(tuple(x))
