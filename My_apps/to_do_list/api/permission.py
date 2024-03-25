from rest_framework import permissions
from to_do_list.models import Project,Task,TeamMember,Comments
class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.created_by == request.user
    
class IsAssigneeorTeammaberOrOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        pk = view.kwargs.get('pk')
        team = None
        if pk:
           team = TeamMember.objects.filter(project = obj.project)
           final = team.filter(user = request.user).exists()
           print(final)
        return obj.assigned_to == request.user or final