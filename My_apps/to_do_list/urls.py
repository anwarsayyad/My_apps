from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name='to-do-home')
]