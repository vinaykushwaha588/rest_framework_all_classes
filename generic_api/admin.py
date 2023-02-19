from django.contrib import admin
from .models import Book
# Register your models here.

@admin.register(Book)
class BookAdminModel(admin.ModelAdmin):
    list_display = ['book_name','publish_date','updated_date']
