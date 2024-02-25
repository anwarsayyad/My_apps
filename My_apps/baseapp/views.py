from django.shortcuts import render

# Create your views here.

def myapphome(request):
    return render(request, 'baseapp/home.html')