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