import  mysql.connector

# Mo ket noi
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="xuan",
    database="mydatabase"
)

# Chuan bi doi tuong cursor
mycursor=mydb.cursor()

sql="drop table if exists customers"

#Thuc thi truy van, xoa bang neu bang do ton tai
mycursor.execute(sql)

#dong ket noi
mydb.close()