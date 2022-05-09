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

sql="update customers set address = 'Canyoun 123' where address = 'Valley 345'"

#update
mycursor.execute(sql)

#comeit
mydb.commit()

# neu upate thanh cong, in ra man hinh
print(mycursor.rowcount,"record(s) affected")

#dong ket noi
mydb.close()