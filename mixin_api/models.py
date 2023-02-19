from pyexpat import model
from django.db import models

# Create your models here.
from django.db import models

# Create your models here.

class Book(models.Model):
    book_name = models.CharField(max_length=100,blank=True,null=True)
    book_title = models.CharField(max_length=150,blank=True,null=True)
    book_author = models.CharField(max_length=100)
    publish_date = models.DateTimeField(auto_now=True)
    updated_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.book_name}'

class Student(models.Model):
    book = models.ForeignKey(Book,on_delete=models.CASCADE,related_name='student')
    stu_name = models.CharField(max_length=100)
    help = models.TextField(max_length=300,blank=True,null=True)
    


    def __str__(self):
        return self.stu_name