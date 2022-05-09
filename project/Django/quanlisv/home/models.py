from django.db import models

# Create your models here.
class Person(models.Model):
    name= models.CharField(max_length=200)
    age=models.IntegerField()
    sex=models.CharField(max_length=4)
    phone=models.IntegerField()
    address=models.CharField(max_length=200)

    class Meta:
        abstract=True

class Student(Person):
    StudentID=models.AutoField(primary_key=True)
    ClassName=models.CharField(max_length=200)
    def __str__(self):
        return self.name