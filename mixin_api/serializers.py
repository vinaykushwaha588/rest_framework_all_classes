from dataclasses import field
from django.db import models
from rest_framework import serializers
from .models import Book,Student

class BookSerializer(serializers.ModelSerializer):
    # student = serializers.StringRelatedField(many=True,read_only=True)
    class Meta:
        model = Book
        fields=['id','book_name','book_title','book_author']


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id','stu_name','help','student']
    # def create(self, validated_data):
    #     obj = Book.objects.create(**validated_data)
    #     obj.save(foo=validated_data['book'])
    #     return obj
    
    # def description(self,book):
    #     return book.name('desciption')