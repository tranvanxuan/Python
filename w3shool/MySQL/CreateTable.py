import  mysql.connector

# Mo ket noi
mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="xuan",
        database="mydatabase"
    )

# Chuan bi mot doi tuong cursor boi su dung phuong thuc cursor
mycursor = mydb.cursor()

#thuc thi truy van SQL
mycursor.execute("CREATE TABLE customers (name VARCHAR (255), address VARCHAR(255))")

# Dong ket noi
mydb.close()

