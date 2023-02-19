from django.db import models

# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=100,blank=True,null=True)
    email = models.EmailField(max_length=100,blank=True,null=True)
    post = models.CharField(max_length=50,blank=True,null=True)
    mobile = models.CharField(max_length=15,blank=True,null=True)

    def __str__(self):
        return self.name