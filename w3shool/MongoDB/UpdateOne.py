# Dung phuong thuc update_one de update 1 ban ghi trong mongoDB
# Chu y neu tim kiem thay nhieu ban ghi, duy nhat ban ghi dau tien duoc update
# update_one(doi tuong can update, gia tri moi cua tai lieu)

import pymongo

# Mo ket noi
myclient=pymongo.MongoClient("mongodb://localhost:27017/")

# tim den co so du lieu
mydb=myclient["mydatabase"]

# tim den bang
mycol=mydb["customers"]

# tham so thu nhat , doi tuong can update
myquery = {"address": "Valley 345"}

# Tham so thu 2 gia tri moi cua ban ghi
newvalues={"$set": {"address": "Canyon 123"}}

# Thuc thi cau lenh
mycol.update_one(myquery,newvalues)

# in customers sau khi upate
for x in  mycol.find():
    print(x)
