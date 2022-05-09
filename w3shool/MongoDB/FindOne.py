import pymongo

# Mo ket noi
myclient = pymongo.MongoClient("mongodb://localhost:27017/")

# chuan bi doi tuong co so du lieu
mydb=myclient["mydatabase"]

# chuan bi doi tuong tai lieu
mycol = mydb["customers"]

# tra ve dong dau tien cua tai lieu
x = mycol.find_one()

# In dong dau tien ra man hinh
print(x)

