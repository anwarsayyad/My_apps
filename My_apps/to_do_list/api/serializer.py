from rest_framework import serializers
from to_do_list.models import Task,Project,Comments,TeamMember

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'
    
class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'

class TeamMemeberSerializers(serializers.ModelSerializer):
    class Meta:
        model = TeamMember
        fields = '__all__'