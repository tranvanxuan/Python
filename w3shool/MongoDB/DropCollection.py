import pymongo

# Mo ket noi
myclient = pymongo.MongoClient("mongodb://localhost:27017/")

# chon csdl
mydb=myclient["mydatabase"]

# chon bang
mycol=mydb["customers"]

mycol.drop()

# Phuong Thuc drop () tra ve true neu bang xoa thanh cong va false neu bang do khong ton tai