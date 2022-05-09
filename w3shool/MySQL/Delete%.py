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
sql="delete from customers where address = %s"

adr=("Yellow Garden 2",)

#thuc thi truy van
mycursor.execute(sql,adr)

#comit thay doi
mydb.commit()

# In ra man hinh
print(mycursor.rowcount, "record(s) delete")

# dong ket noi
mydb.close()