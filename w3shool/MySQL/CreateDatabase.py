import mysql.connector

try:
    # mo ket noi toi co so du lieu
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="xuan"
    )

    # Chuan bi mot doi tuong cursor boi su dung phuong thuc cursor
    mycursor = mydb.cursor()

    # thuc thi truy van sql boi su dung phuong thuc c execute
    mycursor.execute("CREATE DATABASE mydatabase")
    
    mydb.close()

except:
    print("Database da ton tai")
