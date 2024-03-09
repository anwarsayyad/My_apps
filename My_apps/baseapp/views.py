from django.shortcuts import render
from django.views.generic import CreateView
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

from django.views import View

from .forms import UserRegisterForm
# Create your views here.

@login_required
def myapphome(request):
    active = 'home'
    return render(request, 'baseapp/home.html',{
      'active':active   
    })

class Register(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = 'baseapp/Register.html'
    success_url = 'login-page'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["active"] = 'reg' 
        return context
    
    
    def form_valid(self, form):
        response = super().form_valid(form)
        if not form.is_valid():
            print('notvalid')
            return self.render_to_response(self.get_context_data(form = form))
        else:
            print('valid')
            form.save()
        return response
    
    
class Login(View):
    def get(self,request):
        active = 'log'
        return render(request, 'baseapp/login.html',{
            'active':active
        })
    
    def post(self,request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username = username,password = password)
        if user is not None:
            login(request,user)
            return redirect('my-app-home')
        else:
            return redirect('user-register')
    
class AboutMe(View):
    def get(self,request):
        active = 'me'
        return render(request, 'baseapp/aboutme.html',{
            'active' : active
        })
    
    
class Logout(View):
    def get(self, request):
        logout(request)
        return redirect("about-me")