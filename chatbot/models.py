from django.core.validators import RegexValidator
from django.db import models


# Create your models here.

class registration(models.Model):
    branch = models.CharField(max_length=3)
    venue = models.CharField(max_length=20)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    def __str__(self):
        return self.branch

class student(models.Model):
    Name = models.CharField(max_length=100)
    Mail = models.EmailField()
    Roll_No = models.CharField(max_length=9,primary_key=True)
    Branch = models.CharField(max_length=3)
    Room_No = models.CharField(max_length=10)
    Hostel = models.CharField(max_length=12)

    def __str__(self):
        return self.Roll_No
