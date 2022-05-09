# module os cho phep thao tac voi tep va thu muc
import os

# tra ve thu muc lam viec hien tai cua mot tien trinh
print('--------tra ve thu muc hien tai---------')
print(os.getcwd())

print('-----------in ra ta ca tep va thuc muc --------')
# in ra tat ca tep va thu muc hien tai
print(os.listdir())

# in ra tat ca tep thu muc duong dan truyen vao
print('----------in tat ca tep thu muc trong o D------------')
print(os.listdir("D:\\"))

# duyet qua he thong tep
print('----------duyet qua he thong tep walk()-------')
for (root, dirs, files) in os.walk(os.getcwd(), topdown=True):
    print(root)
    print(dirs)
    print(files)
    print('-----------------------')

# tao thu muc
print('--------tao thu muc/ tep o duong dan duoc truyen---------')
#os.mkdir('TEST')
print(os.listdir())

# xoa thu muc
print('-------xoa thu muc -------rmdir()')
os.rmdir('test.py')