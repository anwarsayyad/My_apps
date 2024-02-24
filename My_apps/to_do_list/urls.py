from django.urls import path

from . import views

urlpattens = [
    path("to-do-home/", views.home)
]