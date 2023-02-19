from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import Employee
from .serializers import EmployeeSerializer
from django.http import Http404
from django_filters.rest_framework import DjangoFilterBackend
from .pagination import MyLimiPagination
from rest_framework.generics import ListAPIView
from rest_framework.settings import api_settings
 
# Create your views here.

class EmployeeList(APIView):
    '''This Employee Class are using to GET or POST data'''    
    def get(self,request,format=None):
        emp = Employee.objects.all()
        serializer = EmployeeSerializer(emp, many=True)
        return Response(serializer.data)
    
    def post(self,request, format=None):
        serializer = EmployeeSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


class EmployeeDetails(APIView):
    '''This Employee Class Are Used to UPDATE DELETE OR GET Single Unique records'''
    def get_object(self,id):
        try:
            emp = Employee.objects.get(pk=id)
            return emp
        except Employee.DoesNotExist:
            raise Http404
    def get(self,request,id,format=None):
        emp = self.get_object(id)
        serializer = EmployeeSerializer(emp)
        return Response(serializer.data)

    def put(self,request,id,format=None):
        emp = self.get_object(id)
        serializer = EmployeeSerializer(emp,data=request.data)
        if serializer.is_valid():
            serializer.save()
            res = {'msg':"Employee Updated Successfully.."}
            return Response(res)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def patch(self,request,id,format=None):
        emp = self.get_object(id)
        serializer = EmployeeSerializer(emp,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            res = {'msg':"Employee Partially Updated Successfully.."}
            return Response(res)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,id,format=None):
        emp = self.get_object(id)
        print(emp,'<-----------')
        emp.delete()
        msg = {'msg':'Employee Record Delete Successfully'}
        return Response(msg)

## Define here Paginations 
         
class CustomPagination(ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name', 'email']
    pagination_class = MyLimiPagination


class EmployeeViewSet(APIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    pagination_class = api_settings.DEFAULT_PAGINATION_CLASS

    def get(self,request):
        page = self.paginate_queryset(self.queryset)
        if page is not None:
            serializer = self.serializer_class(page,many=True)
            return self.get_paginated_response(serializer.data)
        else:
            return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)
    @property
    def paginator(self):
        """
        The paginator instance associated with the view, or `None`.
        """
        if not hasattr(self,'_paginator'):
            if self.pagination_class is None:
                self.paginator = None
            else:
                self._paginator = self.pagination_class()
        return self._paginator
    
    def paginate_queryset(self,queryset):
        """
        Return a single page of results, or `None` if pagination is disabled.
        """
        if self.paginator is None:
             return None 
        return self.paginator.paginate_queryset(queryset, self.request, view=self)

    def get_paginated_response(self, data):
         """
         Return a paginated style `Response` object for the given output data.
         """
         assert self.paginator is not None
         return self.paginator.get_paginated_response(data) 
