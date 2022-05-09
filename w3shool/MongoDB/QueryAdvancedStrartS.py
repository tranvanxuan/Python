## Tim kiem tai lieu co truong dia chi bat dau bang 'S', dung {"$regex": "^S"}:
import pymongo

# Mo ket noi
myclient=pymongo.MongoClient("mongodb://localhost:27017/")

# chon csdl
mydb=myclient["mydatabase"]

# chon bang
mycol=mydb["customers"]

## Tim kiem tai lieu co truong dia chi bat dau bang 'S' hay lon hon , dung {"$gt": "S"}:
myquery={"address": {"$regex": "^S"}}

#thuc thi truy van
mydoc=mycol.find(myquery)

# In ra man hinh
for x in mydoc:
    print(x)