from django.contrib import admin
from .models import Book,Student

# Register your models here.
@admin.register(Book)
class BookAdminModel(admin.ModelAdmin):
    list_display = ['book_name','publish_date','updated_date']

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id','help']