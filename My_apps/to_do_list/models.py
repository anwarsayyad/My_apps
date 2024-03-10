from django.db import models
from django.conf import settings

# Create your models here.

status = models.TextChoices("Status", "Planned Working_On Completed Canceled")


class Task(models.Model):
    task_name = models.CharField(max_length=200)
    due_date = models.DateField(null = True)
    task_status = models.CharField(max_length = 200,choices=status.choices)
    created_on = models.DateTimeField(auto_now = True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete = models.CASCADE, null=True)
    

    class Meta:
        verbose_name = ("Task")
        verbose_name_plural = ("Tasks")

    def __str__(self):
        return f"{self.task_name} {self.task_status} {self.created_by}"


