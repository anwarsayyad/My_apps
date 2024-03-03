from django.db import models

# Create your models here.

status = models.TextChoices("Status", "WorkingOn Completed Canceled")

class User(models.Model):
    user_name = models.CharField(max_length = 50)
    

    class Meta:
        verbose_name = ("User")
        verbose_name_plural = ("Users")

    def __str__(self):
        return self.user_name

class Task(models.Model):
    task_name = models.CharField(max_length=200)
    due_date = models.DateField(null = True)
    task_status = models.CharField(max_length = 200,choices=status.choices)
    created_on = models.DateTimeField(auto_now = True)
    created_by = models.ForeignKey(User,on_delete = models.CASCADE, null=True)
    

    class Meta:
        verbose_name = ("Task")
        verbose_name_plural = ("Tasks")

    def __str__(self):
        return f"{self.task_name} {self.task_status} {self.created_by}"


