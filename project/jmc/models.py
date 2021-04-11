from django.db import models

# Create your models here.
class Student(models.Model):
    address = models.CharField(max_length=100)
    img = models.ImageField(upload_to='directory/img')
    lName = models.CharField(max_length=100)
    fName = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    contact = models.IntegerField()
    course = models.CharField(max_length=100)

    def __str__(self):
        return self.fName

class Teacher(models.Model):
    address = models.CharField(max_length=100)
    img = models.ImageField(upload_to='directory/img')
    lName = models.CharField(max_length=100)
    fName = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    contact = models.IntegerField()
    course = models.CharField(max_length=100)

    def __str__(self):
        return self.fName