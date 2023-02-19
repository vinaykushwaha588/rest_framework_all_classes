import imp
from django.urls import path

from .views import *
# BASEURLS = http//127.0.0.1:8000/genericapi/

urlpatterns = [
    path('',ShowView.as_view()),
    path("book/", BookList.as_view(), name="book_list"),
    path("update/<int:pk>/", Book_Update.as_view(), name="book_update"),
    path('retrieve/<int:pk>/',RetrieveDeleteItem.as_view())
]
