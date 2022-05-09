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
mycursor.execute("select name, address from customers")

# Tra ve tat ca cac hang cua tap ket qua truy van
myresult = mycursor.fetchall()

for x in myresult:
    print(x)

# Dong ket noi
mydb.close()