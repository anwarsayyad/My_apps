# To Do App
- basic steps create urls.py file and edit main urls.py file and `include(to_do_list.urls)`
```py
# Main project urls.py file
"""
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('todo/', include("to_do_list.urls")),
    path("",include("baseapp.urls"))
]

```

- urls file in the todoapp
```py
#--urls.py file in the To Do App
from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name='to-do-home'),
    path("create-task",views.createTask.as_view(), name= 'create-task'),
    path("task-list",views.TaskList.as_view(), name='task-list')
]
```
- now lets see views after getting request from browser url file wil execute appropirate views function or class  each request will either `POST` or `GET`

```py
#-----> views.py(to_do_list)
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
```
Here we imported required Django models that are in built
```py
from django.shortcuts import render
from django.views.generic import CreateView, ListView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
```
`CreateView` is imported from django generic class and its very userfull to render the forms and save the data to database with less effor from our end similarly `ListView` is used to extract data from database and render into our template

`loginRequired` is decorators this also Django library it wont allow user to access application functionality without doing login and this used on the above of function as decorators and for class we have to user `LoginRequiredMixin` 

now lets see the models that are creating and updating data in the database
```py
#------> models.py (todoapp)
from django.db import models
from django.conf import settings

# Create your models here.

status = models.TextChoices("Status", "WorkingOn Completed Canceled")


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

```
Imported `settings` to add User model instance to as foriengn key to our model (one to many) as one user can create multiple tasks and task will be renderd according to the user
to access in site

