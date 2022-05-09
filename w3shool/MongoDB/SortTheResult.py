# Phuong thuc Sort ("ten truong", huong) : mac dinh la tang dan
import pymongo

# Mo ket noi
myclient=pymongo.MongoClient("mongodb://localhost:27017/")

# Chon database
mydb=myclient["mydatabase"]

# chon bang
mycol=mydb["customers"]

# Sap xep ket qua tang dan theo name
mydoc=mycol.find().sort("name",1)

# Sap xep ket qua giam theo name
mydoc1=mycol.find().sort("name",-1)

# In ra man hinh
for x in mydoc:
    print(x)
print("---------------------------------------------------------------------")
for y in mydoc1:
    print(y)
