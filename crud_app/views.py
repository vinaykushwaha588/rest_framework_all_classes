from tkinter import E
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import StudentSerializer
from .models import Student
from rest_framework import status
from django.http import Http404
from rest_framework.generics import ListAPIView
from .mypagination import MyLimiPagination
from django_filters.rest_framework import DjangoFilterBackend
# Create your views here.

@api_view(['GET'])

def show_api(request):
    data = Student.objects.all()
    serializer = StudentSerializer(data,many=True)
    return Response(serializer.data,status=status.HTTP_200_OK)


@api_view(["POST"])
def post_api(request):
    serializer = StudentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        res = {'msg':'Student Data is Created Successfully..'}
        return Response(res,status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)

@api_view(['GET','PUT','DELETE'])
def update_delete_api(request,sid):
    try:
        student = Student.objects.get(id=sid)
    except Exception as e:
        print(e)
        raise Http404
    
    if request.method=="GET":
        serilizer=StudentSerializer(student)
        return Response(serilizer.data)

    elif request.method=="PUT":
        serilizer = StudentSerializer(student,data=request.data)
        if serilizer.is_valid():
            serilizer.save()
            res = {'msg':'Student Record Updated Successfully'}
            return Response(serilizer.data,status=status.HTTP_200_OK)
        else:
            return Response(serilizer.errors,status=status.HTTP_404_NOT_FOUND)
    
    elif request.method=="DELETE":
        student.delete()
        res = {'msg':"Student Data Deleted Successfully.."}
        return Response(res)

class EmployeeList(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['email']
    pagination_class = MyLimiPagination
    
