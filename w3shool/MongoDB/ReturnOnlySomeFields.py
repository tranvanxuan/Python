### Chu y Ban khong the chi dinh ca 2 gia tri 0 va 1 cho cung mot doi tuong (ngoai tru tuong _id)
# Neu ban chi dinh mot truong gia tri 0 , thi tat cac cac truong con lai gia tri 1 va nguoc lai
import pymongo

# Mo ket noi
myclient=pymongo.MongoClient("mongodb://localhost:27017/")

# khoi tao doi tuong database
mydb=myclient["mydatabase"]

# Khoi doi tuong bang
mycol=mydb["customers"]

# Tham so thu 2 cua phuong thuc find() la cac truong ban muon dua vao trong ket qua
# tra ve cot ten va dia chi
for x in mycol.find({},{"_id" : 0, "name" : 1, "address" : 1}):
    print(x)

for y in mycol.find({},{  "address" : 0}):
    print(y)
