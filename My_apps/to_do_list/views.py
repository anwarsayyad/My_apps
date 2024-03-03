from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import CreateView, ListView

from .forms import TaskForm
from .models import Task

# Create your views here.

def home(request):
    return render(request, "to_do_list/home.html")

class createTask(CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'to_do_list/create_task.html'
    success_url = 'create-task'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    
class TaskList(ListView):
    template_name = "to_do_list/tasks_list.html"
    model = Task
    context_object_name = 'tasks'

    # def get_queryset(self) -> QuerySet[Any]:
    #     base_query = super().get_queryset()
    #     data = base_query.filter(created_by = 1)
    #     return data