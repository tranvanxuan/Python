import pymongo

# Mo ket noi
myclient=pymongo.MongoClient("mongodb://localhost:27017/")

# tim den co so du lieu
mydb=myclient["mydatabase"]

# tim den bang
mycol=mydb["customers"]

# tham so thu nhat , doi tuong can update
myquery = {"address": {"$regex": "^O"}}

# Tham so thu 2 gia tri moi cua ban ghi
newvalues={"$set": {"name": "Minnie"}}

# upate nhung ban ghi co dia chi bat dau bang O thanh ten Minnie
x = mycol.update_many(myquery,newvalues)

# in so ban ghi duoc update
print(x.modified_count, " documents updated.")
