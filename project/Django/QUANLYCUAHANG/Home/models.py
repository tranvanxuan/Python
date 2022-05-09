from django.db import models


# Create your models here.
class CuaHang(models.Model):
    Ten_Cua_Hang=models.CharField(max_length=500)
    Ma_Cua_Hang=models.CharField(max_length=50)
    Dia_Chi=models.CharField(max_length=500)
    Ngay_Tao= models.DateTimeField('publish date')
    def __str__(self) -> str:
        return self.Ten_Cua_Hang
class SanPham(models.Model):
    Ten_San_Pham=models.CharField(max_length=500)
    Ma_San_Pham=models.CharField(max_length=50)

class Customer(models.Model):
    CustomerId=models.AutoField(primary_key=True)
    Ten_Khach_Hang=models.CharField(max_length=200)
    Ma_Khach_Hang=models.CharField(max_length=50)

class CustomerInfor(models.Model):
    CustomerInfoId=models.AutoField(primary_key=True)
    CMND=models.CharField(max_length=500)
    CustomerId=models.ForeignKey(Customer,on_delete=models.CASCADE)

    # chu y meta dung de cau hinh
    # https://docs.djangoproject.com/en/4.0/ref/models/options/

    # thua ke tu lop truu tuong
    # thua ke da bang 
    # dung lop Proxy
    class Meta:
        ordering= ["CustomerInfoId"]

class Calculate(models.Model):
    Number1=models.IntegerField()
    Number2=models.IntegerField()

    class Meta:
        abstract=True#De la 1 lop truu tuong abstract = True
        ordering= ["Number1"]

class  Caculator(Calculate):# Caculator khong phai la lop truu tuong 
    #vi khi ke thua tu calculate django da tao bien abstract la fale, 
    # sau khi ke thua het moi abstract = true
    total=models.IntegerField()

class Author(models.Model):
    authorID=models.AutoField(primary_key=True)
    name=models.CharField(max_length=200)
    email=models.EmailField()
    phone=models.IntegerField()
    def __str__(self):
        return self.name

class Book(models.Model):
    bookid=models.AutoField(primary_key=True)
    name=models.CharField(max_length=200)
    title=models.CharField(max_length=200)
    authorid=models.ForeignKey(Author, on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class Store(models.Model):
    storeid=models.AutoField(primary_key=True)
    bookid=models.ForeignKey(Book, on_delete=models.CASCADE)
    name=models.CharField(max_length=200)
    def __str__(self):
        return self.name
        