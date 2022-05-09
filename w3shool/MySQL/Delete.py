import mysql.connector

# Mo ket noi
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="xuan",
    database="mydatabase"
)

#Chuan bi doi tuong cursor
mycursor=mydb.cursor()

# sql
sql="delete from customers where address='Mountain 21'"

#thuc thi truy van
mycursor.execute(sql)

#comit thay doi
mydb.commit()

# In ra man hinh
print(mycursor.rowcount, "record(s) delete")

# dong ket noi
mydb.close()