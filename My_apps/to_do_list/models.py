from django.db import models
from django.conf import settings

# Create your models here.

status = models.TextChoices("Status", "Assigned Working_On Resolved Canceled")
priority = models.TextChoices("Priority","P1 P2 P3 P4")

class Project(models.Model):
    name = models.CharField(max_length=50, unique = True)
    description = models.TextField()
    start_date = models.DateField(auto_now=True)
    end_date = models.DateField(auto_now=False)    
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    class Meta:
        verbose_name = ("Project")
        verbose_name_plural = ("Projects")

    def __str__(self):
        return self.name

class TeamMember(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.user}"

    class Meta:
        verbose_name = ("TeamMember")
        verbose_name_plural = ("TeamMembers")


class Task(models.Model):
    task_name = models.CharField(max_length=200,unique=True)
    project = models.ForeignKey(Project,on_delete=models.CASCADE,null =True)
    due_date = models.DateField(null = True)
    task_status = models.CharField(max_length = 200,choices=status.choices, default = 'Planned')
    created_on = models.DateTimeField(auto_now = True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete = models.CASCADE, null=True)
    assigned_to = models.ForeignKey(TeamMember, on_delete=models.CASCADE, null= True)
    priority_level = models.CharField(max_length = 50, choices = priority.choices, null =True)

    class Meta:
        verbose_name = ("Task")
        verbose_name_plural = ("Tasks")

    def __str__(self):
        return f"{self.task_name} {self.task_status} {self.created_by}"
    
class Comments(models.Model):
    Comments = models.TextField()
    attachement = models.FileField( upload_to='Tasks_app', max_length=100)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete = models.CASCADE, null=True)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.Comments} {self.task} {self.created_by}'
    class Meta:
        verbose_name = ("Comments")
        verbose_name_plural = ("Commentss")



    







