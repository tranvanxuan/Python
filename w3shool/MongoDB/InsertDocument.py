#De them mot ban ghichung ta phuong thuc insert_one()
import pymongo

# Mo ket noi
myclient=pymongo.MongoClient("mongodb://localhost:27017/")

# Tao co so du lieu
mydb=myclient["mydatabase"]

# Tao bo suu tap
mycol=mydb["customers"]

# tao mot tu dien
mydict={"name":"John", "address":"Highway 37"}

# tham so dau tien cua phuong truc insert_onet la mot tu dien chua ten
# va gia tri cua tung truong trong tai lieu ban muon tao
x = mycol.insert_one(mydict)

#Tra ve ID cua tai lieu duoc them vao
# thuoc tinh inserted_id cua phuong thuc insert_one
print(x.inserted_id)