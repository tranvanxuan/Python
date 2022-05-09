import pymongo

# Mo ket noi
myclient = pymongo.MongoClient("mongodb://localhost:27017/")

# chon csdl
mydb=myclient["mydatabase"]

# chon bang
mycol=mydb["customers"]

# doi tuong truy van
myquery={"address": "Mountain 21"}

# thuc thi truy van
# neu query tim thay nhieu hon mot ban ghi, thi chi co ban ghi duy nhat bi xoa
mycol.delete_one(myquery)

# in ra man hinh neu con tim thay ban ghi
for x in mycol.find():
    print(x)