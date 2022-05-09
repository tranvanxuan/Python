#Gioi han ket qua tra ve dung cau lenh LIMIT
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

#lay ra 5 ban ghi dau tien trong bang customers
mycursor.execute("select * from customers LIMIT 5")

# Tra ve tat ca cac hang cua tap ket qua truy van
myresult = mycursor.fetchall()

for x in myresult:
    print(x)

# Dong ket noi
mydb.close()