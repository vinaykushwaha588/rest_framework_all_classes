
from django.db import models


# Create your models here.
class Library(models.Model):
    b_name = models.CharField(max_length=100)
    b_title = models.CharField(max_length=300)
    b_author = models.CharField(max_length=50)
    publish_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.b_name

class Student(models.Model):
    library = models.ForeignKey(Library,on_delete=models.CASCADE)
    stu_name = models.CharField(max_length=100)
    help = models.TextField(max_length=300)


    def __str__(self):
        return self.stu_name

  
    