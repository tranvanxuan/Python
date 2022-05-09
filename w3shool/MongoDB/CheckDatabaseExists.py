import pymongo

# Mo ket noi
myclient = pymongo.MongoClient("mongodb://localhost:27017/")

# # tra ve danh sach cac co so du lieu co trong he thong
# print(myclient.list_database_names())

# tao doi tuong
dblist=myclient.list_database_names()

# kiem tra database da ton tai chua
if"mydatabase" in dblist:
    print("The database exists.")