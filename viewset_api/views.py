from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework import viewsets
from viewset_api.models import Library,Student
from viewset_api.serializers import LibrarySerializers,StudentSerializer
# Create your views here.

class LibraryViewSet(viewsets.ViewSet):                                                                                             
    def list(self,request):
        lib = Library.objects.all()
        print(lib,"<------")
        serializer = LibrarySerializers(lib,many=True)
        print(serializer.data,"<---------")
        return Response(serializer.data,status=status.HTTP_200_OK)

    def retrieve(self,request,pk=None):
        id=pk
        if id is not None:
            lib = Library.objects.get(id=id)
            serializer = LibrarySerializers(lib)
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)

    def create(self,request):
        serializer = LibrarySerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)  

    def update(self,request,pk):
        id=pk
        lib = Library.objects.get(pk=id)   
        serializer = LibrarySerializers(lib,data=request.data)   
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':"Library Record Updated Successfully"})
        else:
            return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)
    def delete(self,request,pk):
        id=pk
        lib = Library.objects.get(pk=id)
        lib.delete()
        return Response({'msg':"Library Record Deleted Successfully"})
        
## Here I Created ModelAPIViewset Classes

class LibViewSet(viewsets.ModelViewSet):
    queryset = Library.objects.all()
    serializer_class = LibrarySerializers


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer