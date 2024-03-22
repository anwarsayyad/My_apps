"""
URL configuration for My_apps project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from rest_framework import routers,serializers,viewsets
from django.contrib.auth.models import User
from to_do_list.api.views import TaskViewset

#Serializers define the API representaion
class UserSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email','is_staff']

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializers
    
router = routers.DefaultRouter()
router.register(r'tasks',TaskViewset,basename='taskapi')
router.register(r'users',UserViewSet,basename='usersapi')
urlpatterns = [
    path('admin/', admin.site.urls),
    path('todo/', include("to_do_list.urls")),
    path("",include("baseapp.urls")),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include(router.urls)),
    path('api/custom/', include('to_do_list.api.urls'))
]
