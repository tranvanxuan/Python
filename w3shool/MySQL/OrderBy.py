#Sap xep ket qua tang dan hoac giam dan
import mysql.connector

# Mo ket noi
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="xuan",
    database="mydatabase"
)

# Chuan bi doi tuong curoser
mycursor=mydb.cursor()

#tao doi tuong sql
sql="select * from customers order by name"

# Thuc thi truy van
#mac dinh la sap xem tang dan
mycursor.execute(sql)

# Hien thi tat ca ban ghi cua tap ket qua tra ve
myresult=mycursor.fetchall()

#in ket qua ra man hinh
for x in myresult:
    print(x)

# Dong ket noi
mydb.close()
