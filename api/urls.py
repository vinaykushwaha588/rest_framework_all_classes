from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include('student.urls')),
    path('crudapi/',include('crud_app.urls')),
    path("viewsetapi/", include('viewset_api.urls')),
    path('genericapi/',include('generic_api.urls')),
    path('mixinapi/',include('mixin_api.urls')),
    
]
