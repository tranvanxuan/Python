# Ban co the lay duoc id cua dong ban them vao boi doi tuong cursor
#Neu ban them vao 1 dong, id cua dong cuoi cung se duoc tra ve
import  mysql.connector

# Mo ket noi
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="xuan",
    database="mydatabase"
)

# Chuan bi doi tuong cursor
mycursor=mydb.cursor()

#Cau lenh sql

sql = "INSERT INTO CUSTOMERS (NAME,ADDRESS) VALUES (%s , %s)"

val=("Michelle","Blue Village")

#thuc thi truy van sql
mycursor.execute(sql,val)

# Chu y !!! Cau lenh thuc hien su thay doi voi bang neu khong khong co su thay doi nao
mydb.commit()

# tra ve ID dong cuoi cung
print("1 record inserted, ID:",mycursor.lastrowid)

#Dong ket noi
mydb.close()