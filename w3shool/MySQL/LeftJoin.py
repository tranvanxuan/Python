# Neu ban muon hien thi tat ca nguoi dung, ngay ca khi khong co san pham yeu thiech  , dung left join
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

sql="select  users.name as user, products.name as favorite from users right join products on  users.fav = products.id "


#thuc thi truy van SQL
mycursor.execute(sql)

myresult=mycursor.fetchall()

for x in myresult:
    print(x)

# Dong ket noi
mydb.close()

