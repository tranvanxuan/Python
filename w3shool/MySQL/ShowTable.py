import  mysql.connector

# mo ket noi
mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="xuan",
        database="mydatabase"
    )

# Chuan bi doi tuong cursor
mycursor = mydb.cursor()

# Thuc thi truy van mysql
mycursor.execute("show tables")

# hien thi tat ca bang trong db
for x in mycursor:
    print(x)

#Dong ket noi
mydb.close()