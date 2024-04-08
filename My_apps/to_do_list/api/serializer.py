from rest_framework import serializers
from to_do_list.models import Task,Project,Comments,TeamMember
from django.contrib.auth.models import User



class TeamMemeberSerializers(serializers.ModelSerializer):
    class Meta:
        model = TeamMember
        fields = '__all__'
        
class TaskSerializer(serializers.ModelSerializer):
    project = serializers.PrimaryKeyRelatedField(queryset = Project.objects.all())
    created_by = serializers.PrimaryKeyRelatedField(queryset = User.objects.all())
    assigned_to = TeamMemeberSerializers()
    class Meta:
        model = Task
        fields = '__all__'
    
class ProjectSerializer(serializers.ModelSerializer):
    created_by = serializers.StringRelatedField()
    class Meta:
        model = Project
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = '__all__'