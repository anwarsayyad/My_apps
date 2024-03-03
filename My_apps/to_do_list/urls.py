from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name='to-do-home'),
    path("create-task",views.createTask.as_view(), name= 'create-task'),
    path("task-list",views.TaskList.as_view(), name='task-list')
]