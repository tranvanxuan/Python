#Gioi han ket qua tra ve dung cau lenh LIMIT
#Neu ban muon tra ve 5 ban ghi, bat dau tu ban ghi thu 3 dung tu khoa OFFSET
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

#lay ra 5 ban ghi tu ban ghi thu 3
mycursor.execute("select * from customers LIMIT 5 OFFSET 2")

# Tra ve tat ca cac hang cua tap ket qua truy van
myresult = mycursor.fetchall()

for x in myresult:
    print(x)

# Dong ket noi
mydb.close()