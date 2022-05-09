# De gioi han ket qua tra ve trong mongoDB , chung ta dung phuong thuc limit()
# Phuong thuc limit() co mot tham so, so ban ghi
import pymongo

# Mo ket noi
myclient=pymongo.MongoClient("mongodb://localhost:27017/")

# tim den co so du lieu
mydb=myclient["mydatabase"]

# tim den bang
mycol=mydb["customers"]

# Gioi han ket qua tra ve duy nhat 5 ban ghi
myresult=mycol.find().limit(5)

# in 5 ban ghi ra man hinh
for x in myresult:
    print(x)