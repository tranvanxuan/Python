import mysql.connector


# mo ket noi toi co so du lieu
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="xuan"
)

# Chuan bi mot doi tuong cursor boi su dung phuong thuc cursor
mycursor = mydb.cursor()

#thuc thi truy van su dung phuong thuc execute()
mycursor.execute("show databases")

#hien thi danh sach co so du lieu

for x in mycursor:
    print(x)

mydb.close()