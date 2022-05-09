import pymongo

# Mo ket noi
myclient = pymongo.MongoClient("mongodb://localhost:27017/")

# chon csdl
mydb=myclient["mydatabase"]

# chon bang
mycol=mydb["customers"]

# thuc thi truy van
x=mycol.delete_many({})

# in ra man binh tong so ban ghi bi xoa
print(x.deleted_count," documents deleted.")