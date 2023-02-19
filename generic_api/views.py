from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Book
from .serializers import BookSerializer
from rest_framework import generics

# Create your views here.

class ShowView(APIView):
    def get(self,request):
        return Response("This is GENENICS_API_Class View")

class BookList(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
   

class Book_Update(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

from rest_framework.generics import GenericAPIView
## Creating Here GenericAPIView class 

class RetrieveDeleteItem(GenericAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()

    def get(self,request,*args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
  
    
    def delete(self,request,*args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
