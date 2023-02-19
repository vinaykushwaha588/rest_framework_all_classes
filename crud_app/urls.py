from django.urls import path
from .views import *

## Base URL = http//127.0.0.1:8000/api/

urlpatterns = [
    path('get/',show_api),
    path("post/", post_api),
    path('update-delete/<int:sid>/',update_delete_api),
    path('filter/',EmployeeList.as_view()),
    
]
