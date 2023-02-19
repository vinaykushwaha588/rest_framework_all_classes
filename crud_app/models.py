import email
from pyexpat import model
from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100,blank=True,null=True)
    email = models.EmailField(max_length=100,null=True,blank=True)
    mobile = models.CharField(max_length=15,blank=True,null=True)
    age = models.IntegerField(blank=True,null=True)

    def __str__(self):
        return f'{self.name}'