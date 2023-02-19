from django.urls import path
from .views import *
# BASEURL = http//127.0.0.1:8000/mixinapi//

urlpatterns = [
    path('',BookList.as_view()),
    path('update/<int:pk>/',BookDetails.as_view())
]
