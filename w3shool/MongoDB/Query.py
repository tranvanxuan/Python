import pymongo

# Mo ket noi
myclient=pymongo.MongoClient("mongodb://localhost:27017/")

#  Chon co so du lieu
mydb=myclient["mydatabase"]

# chon bang
mycol=mydb["customers"]

# Khoi tao doi tuong truy van
myquery={"address" : "Park Lane 38"}

# Loc ket qua
mydoc=mycol.find(myquery)

for x in mydoc:
    print(x)

