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

val=("John","Highway 21")

#thuc thi truy van sql
mycursor.execute(sql,val)

# Chu y !!! Cau lenh thuc hien su thay doi voi bang neu khong khong co su thay doi nao
mydb.commit()

# in du lieu ra man hinh
print(mycursor.rowcount,"recordinserted.")

#Dong ket noi
mydb.close()