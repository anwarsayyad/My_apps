from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import generics, renderers
from rest_framework import viewsets
from to_do_list.models import Task
from to_do_list.api.serializer import TaskSerializer
from rest_framework import permissions
from to_do_list.api.permission import IsOwnerOrReadOnly




class Sort(APIView):
    def get(self,request,format='application/json'):
        tasks = Task.objects.all().order_by('due_date')
        serialzer = TaskSerializer(tasks,many=True)
        return Response(serialzer.data,status=status.HTTP_200_OK)
            
# class testGeneric(generics.ListCreateAPIView):
#     queryset = Task.objects.all()
#     serializer_class = TaskSerializer
    
#     def post(self, request, *args, **kwargs):
#         tasks = self.serializer_class(data = request.data)
#         if tasks.is_valid(raise_exception=True):
#             tasks.save()
#             return Response(tasks.data,status=status.HTTP_201_CREATED)
#         return Response(tasks.errors.get('task_name'),status=status.HTTP_400_BAD_REQUEST)
# class testGeneric2(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Task.objects.all()
#     serializer_class = TaskSerializer
    
class StatusTask(generics.ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def get(self, request, *args, **kwargs):
        arg = kwargs.get('task_name')
        if arg:
            self.queryset = self.queryset.filter(task_name = arg)
        return super().get(request, *args, **kwargs)
    
class TaskViewset(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly]
    
    def perform_create(self, serializer):
        serializer.save(created_by = self.request.user)
    
    