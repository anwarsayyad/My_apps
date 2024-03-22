from typing import Any, Mapping
from django import forms
from django.core.files.base import File
from django.db.models.base import Model
from django.forms.utils import ErrorList
from django.utils.timezone import is_aware,make_aware
from datetime import date,datetime

from .models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        exclude = ["created_on",'created_by','task_status']
    
    def clean_scheduled(self):
        date_value = self.cleaned_data.get('scheduled')
        due = self.cleaned_data.get('due_date')
            
        due = datetime.combine(due, datetime.min.time())
        date_value = datetime.combine(date_value, datetime.min.time())
        
        if date_value < datetime.now() or date_value.date() > due:
            raise forms.ValidationError("Scheduled date cannot be in the past or greater than due date")
        return date_value
class TaskFormKUpdateTask(forms.ModelForm):
    def __init__(self,*args, **kwargs):
        super(TaskFormKUpdateTask, self).__init__(*args, **kwargs)
        for field_name , field in self.fields.items():
            if field_name != 'task_status':
                field.widget.attr['readonly'] = True
                field.widget.attr['disabled'] = True 
    class Meta:
        model = Task
        fields = '__all__' 


        

    
