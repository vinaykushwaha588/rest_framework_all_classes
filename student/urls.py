from django.urls import path
from .views import *
## Base urls = http//127.0.0.1.8000/api/

urlpatterns = [
    path('get-post/',EmployeeList.as_view()),
    path('update-delete/<int:id>/',EmployeeDetails.as_view()),
    path('filter/',CustomPagination.as_view()),
    path('filter1/',EmployeeViewSet.as_view())
]
