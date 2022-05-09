# Mot bo suu tap trong mongodb giong nhu bang trong sql
#trong mongo mot bo suu tap khong duoc tao cho den khi no co noi dung
import pymongo

# Mo ket noi
myclient=pymongo.MongoClient("mongodb://localhost:27017/")

# Tao co so du lieu
mydb=myclient["mydatabase"]

# Tao bo suu tap
mycol=mydb["customers"]

# in danh sach bang trong co so du lieu
print(mydb.list_collection_names())

#dong ket noi
myclient.close()