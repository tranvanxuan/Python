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

#Thuc thi cau lenh
mycursor.execute("select * from customers")

# Tra ve dong dau tien cua ket qua
myresult = mycursor.fetchone()

print(myresult)
# Dong ket noi
mydb.close()