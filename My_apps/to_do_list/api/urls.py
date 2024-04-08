from django.urls import path
from . import views

urlpatterns = [
  
    path('sort/', views.Sort.as_view()),
    path('<str:task_name>/',views.StatusTask.as_view())

]