from logging import addLevelName
from django.contrib import admin
from .models import Library,Student
# Register your models here.

@admin.register(Library)
class LibraryModelAdmin(admin.ModelAdmin):
    list_display = ['b_name','b_title','publish_date']

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['stu_name','help']