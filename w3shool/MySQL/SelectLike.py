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

# khoi tao doi tuong
sql="select * from customers where address like '%way%'"

#Thuc thi truy van
mycursor.execute(sql)

#Tra ve tat ca cac dong cua tap ket qua
myresult=mycursor.fetchall()

#chay vong lap va in ket qua ra man hinh
for x in myresult:
    print(x)

# Dong ket noi
mydb.close()