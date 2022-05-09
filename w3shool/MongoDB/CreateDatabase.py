### Quan trong trong MongoDB co so du lieu khong duoc tao cho den khi co noi dung
import  pymongo

# Mo ket noi
myclient = pymongo.MongoClient("mongodb://localhost:27017/")

#co so du lieu khong doc tao cho den khi co noi dung
mydb=myclient["mydatabase"]

