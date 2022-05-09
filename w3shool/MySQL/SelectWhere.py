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

sql="select * from customers where address = 'Park Lane 38'"

#thuc thi truy van
mycursor.execute(sql)

# fetchall tra ve tat ca cac dong cua tap truy van
myresult=mycursor.fetchall()

# in ket qua ra amn hinh
for x in myresult:
    print(x)

# Dong ket noi
mydb.close()