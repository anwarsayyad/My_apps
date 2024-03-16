from rest_framework import serializers
from to_do_list.models import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id','task_name','due_date','task_status','created_by']