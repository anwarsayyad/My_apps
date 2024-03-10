from django.shortcuts import render
from django.views.generic import CreateView, ListView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


from .forms import TaskForm
from .models import Task

# Create your views here.
@login_required
def home(request):
    active_link = 'home'
    tasks = Task.objects.filter(created_by = request.user)
    username = request.user.username
    print(username)
    return render(request, "to_do_list/home.html",{
        'active' :active_link,
        'tasks':tasks
    })

class createTask(LoginRequiredMixin,CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'to_do_list/create_task.html'
    success_url = 'create-task'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        form.save()
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["active"] = 'create'
        return context
    
   
class TaskList(LoginRequiredMixin,ListView):
    template_name = "to_do_list/tasks_list.html"
    model = Task
    context_object_name = 'tasks'
    def get_context_data(self, **kwargs):
         context = super().get_context_data(**kwargs)
         context["active"] = 'list'
         return context
    
    def get_queryset(self):
        task =  super().get_queryset()
        return task.filter(created_by = self.request.user)
    
    
    

    # def get_queryset(self) -> QuerySet[Any]:
    #     base_query = super().get_queryset()
    #     data = base_query.filter(created_by = 1)
    #     return data