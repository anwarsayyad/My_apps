from django.http import HttpResponse , JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view ,  permission_classes
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status
from to_do_list.models import Task
from .serializer import TaskSerializer

@api_view(['GET','POST'])
@permission_classes((permissions.AllowAny,))
def task_list(request):
    if request.method == 'GET':
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many = True)
        return Response(serializer.data)
    
    elif request.method == "POST":
        serializer = TaskSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)