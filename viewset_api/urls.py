from django.urls import path,include
from .views import *
from rest_framework.routers import DefaultRouter

# Creating Router object
router = DefaultRouter()

# Register LibraryViewSet with Router
router.register('viewset',LibraryViewSet,basename='libraryviewset')
router.register('modelviewset',LibViewSet,basename='librarymodelviewset')
router.register('stumodelviewset',StudentViewSet,basename='studentmodelviewset')

##  Base Url - http//127.0.0.1:8000/viewset/

urlpatterns = [
    path('',include(router.urls)),
]
