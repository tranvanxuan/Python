# Ham compile () tra ve nguon duoc chi dinh  duoi dang doi tuong ma , san sang de thuc thi
# x la mot biueu thuc
x=compile('print(55)', 'test', 'eval')

# thuc thi
exec(x)

# Cu phap compile (source, filename,mode,flag,dont_inherit, iptimize)
    # Source : nguon de bien dich, co the la mot chuoi, mot doi tuong Bytes, hay doi tuong AST
    # File name: Ten cua tep nguon, neu nguon khong den tu tep nao, ban co the viet bat cu dieu gi ban thich
    #Mode che do : Gia tri
        #eval neu nguon la mot bieu thuc
        # exec : neu nguon la khoi cau lenh
        # single : neu nguon la mot tuyen bo tuong tac
    # Flag :

# y la mot khoi lenh
y = compile('print(55)\nprint(88)','test','exec')

exec(y)