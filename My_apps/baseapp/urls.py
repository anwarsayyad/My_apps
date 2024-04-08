from django.urls import path
from . import views
urlpatterns = [
    path("",views.AboutMe.as_view(),name="about-me"),
    path("apps",views.myapphome, name = 'my-app-home'),
    path("Register",views.Register.as_view(), name='user-register'),
    path("accounts/login/",views.Login.as_view(),name='login'),
    path("logout",views.Logout.as_view(),name="logout")
]