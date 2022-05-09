import pymongo

# Mo ket noi
myclient = pymongo.MongoClient("mongodb://localhost:27017/")

#tao co so du lieu
mydb=myclient["mydatabase"]

#tao bo suu tap
mycol=mydb["custormers"]

# tao danh sach bo suu tap
collist=mydb.list_collection_names()

if 'customers' in collist:
    print("The  Collection Exists")