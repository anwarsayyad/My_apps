from django.db import models

# Create your models here.
class Task(models.Model):
    task = models.CharField(max_length = 50)
    Due = models.DateTimeField()

    def __str__(self) -> str:
        return f"{self.task} : {self.Due}"