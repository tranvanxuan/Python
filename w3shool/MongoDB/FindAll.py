import pymongo

# Mo ket noi
myclient=pymongo.MongoClient("mongodb://localhost:27017/")

# khoi tao doi tuong database
mydb=myclient["mydatabase"]

# Khoi doi tuong bang
mycol=mydb["customers"]

# Tra ve tat ca doi tuong trong tai lieu

for x in mycol.find():
    print(x)