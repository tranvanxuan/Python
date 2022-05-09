import mysql.connector

# De chen nhieu dong toi mot bang dung phuong thuc executemany()
# Tham so thu 2 cua phuong thuc executemany chua mot bo danh sach du lieu ban muon chen
# Mo chuoi ket noi
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="xuan",
    database="mydatabase"
)

# Chuan bi doi tuong cursor
mycursor = mydb.cursor()

# tham so dau tien, khai bao doi tuong sql
sql = "INSERT INTO CUSTOMERS (NAME,ADDRESS) VALUES(%s, %s)"

# Tham so thu 2
val = [('Peter', 'Lowstreet 4'),
       ('Amy', 'Apple st 652'),
       ('Hannah', 'Mountain 21'),
       ('Michael', 'Valley 345'),
       ('Sandy', 'Ocean blvd 2'),
       ('Betty', 'Green Grass 1'),
       ('Richard', 'Sky st 331'),
       ('Susan', 'One way 98'),
       ('Vicky', 'Yellow Garden 2'),
       ('Ben', 'Park Lane 38'),
       ('William', 'Central st 954'),
       ('Chuck', 'Main Road 989'),
       ('Viola', 'Sideway 1633')
       ]

#Thuc thi truy van
mycursor.executemany(sql,val)

# comit thay doi
mydb.commit()

#In so dong da them vao ra man hnh
print(mycursor.rowcount,"Da duoc them vao")

# Dong ket noi
mydb.close()