#them module
import mysql.connector


# Khoi tao chuoi ket noi
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "xuan",

    #chon mot database cu the
    database = "mydatabase"
)

