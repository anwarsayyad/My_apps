# Base App
This app will be used for the mostly authentication purpose and connected with Django built in `User` Model there we will be storing `User name` ,`email`, `password` 

## User registration 
**form.py**
for this we will be creating form.py file the import Django form modules and other librbries and here is the code
```py
# form.py
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']
```

`UserCreationForm` is the Django built in form and we are importing it creating our own form for registration with fields ` fields = ['username','email','password1','password2']`

**view.py**
later we need to render this form through the `viwes.py` file code will be like
```py
from django.views.generic import CreateView  # for cCreatView class easy render forms and saving
from django.contrib.auth.models import User #Django inbuilt User model 

#---> views.py
class Register(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = 'baseapp/Register.html'
    success_url = 'accounts/login/'
    
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

```

## User registration form
Yes, Django provides an inbuilt user registration form as part of its authentication framework. You can use the `UserCreationForm` class provided by Django to create a user registration form quickly and easily.

Here's how you can use the `UserCreationForm` to create a user registration form:

1. In your Django app, create a forms.py file if you don't already have one.

2. Import the `UserCreationForm` class from `django.contrib.auth.forms`:

```python
from django.contrib.auth.forms import UserCreationForm
```

3. Create a new class for your user registration form, subclassing `UserCreationForm`:

```python
class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email']  # Add any additional fields you want for registration
```

4. Optionally, you can customize the form further by adding additional fields or validation logic as needed.

5. In your views.py file, import the `UserRegistrationForm` and use it in your view function or class-based view:

```python
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegistrationForm

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to login page after successful registration
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})
```

6. Create a template (e.g., register.html) to render the user registration form:

```html
<!DOCTYPE html>
<html>
<head>
    <title>User Registration</title>
</head>
<body>
    <h2>User Registration</h2>
    <form method="post">
        {% csrf_token %}
        {{ form.as_p }}
        <button type="submit">Register</button>
    </form>
</body>
</html>
```

This form will include fields for username, email, and password (twice for confirmation). You can customize the form and template as needed to match your application's requirements.

With this setup, when users submit the registration form, a new user will be created in the database using the provided information, and they will be redirected to the login page.

## User access
By default, the users created using Django's authentication system will not have access to the Django admin portal. Django's authentication system is separate from the admin site, and creating a user using the `UserCreationForm` will not automatically grant them access to the admin site.

To ensure that users created using the registration form do not have access to the admin site, you can remove the `'django.contrib.admin'` app from the `INSTALLED_APPS` setting in your Django project's settings.py file. This will disable the admin site entirely.

```python
INSTALLED_APPS = [
    # 'django.contrib.admin',
    # Other installed apps
]
```

Alternatively, you can restrict access to the admin site by removing or restricting the permissions of the users created using the registration form. By default, new users do not have any special permissions, so they won't be able to access the admin site unless explicitly granted access by a superuser.

You can also customize the admin site's behavior and permissions further by creating custom admin views or overriding the default admin site behavior using Django's admin customization options. However, if you simply want to prevent users from accessing the admin site entirely, removing the admin app from the `INSTALLED_APPS` setting is the simplest approach.

## Adding minimum fields to Form
To create a user who can just use your site without any special permissions or access to the admin portal, you typically only need to collect basic information such as username, email, and password. Here's a basic example of the minimum fields you might include in your user registration form:

1. Username: Allows users to create a unique identifier for themselves.
2. Email: Provides a means of communication and can be used for password recovery.
3. Password (twice for confirmation): Securely authenticate users and protect their accounts.

You can create a user registration form with just these fields using Django's `UserCreationForm` or by creating a custom form with the necessary fields. Here's how you can do it using `UserCreationForm`:

```python
# forms.py

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
```

In this form, `password1` and `password2` are used to collect the user's password and confirm it by entering it twice.

You can then use this form in your view and template to allow users to register on your site. Make sure to customize the template to render the form fields appropriately and handle form submission in your view.

By collecting just these basic fields, users can create accounts and use your site without needing access to the admin portal or any special permissions.

## Using create View class
If you are using Django's `CreateView` to handle the user registration process, you can still check for form validation errors and display them to the user within the context of the `CreateView`. Here's how you can do it:

1. Customize the form validation by overriding the `form_valid` method in your `CreateView`.
2. If the form is not valid, render the form again along with the validation errors.

Here's an example of how you can implement this:

```python
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView

class RegisterView(CreateView):
    template_name = 'register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('login')  # Redirect to login page after successful registration

    def form_valid(self, form):
        # Save the form data and check if it's valid
        response = super().form_valid(form)
        if not form.is_valid():
            # If the form is not valid, re-render the form with errors
            return self.render_to_response(self.get_context_data(form=form))
        return response
```

In this example, the `RegisterView` class is a subclass of Django's `CreateView`. We override the `form_valid` method to customize the form validation logic. If the form is not valid, we render the form again with the validation errors by calling `self.render_to_response(self.get_context_data(form=form))`.

Make sure to adjust the `template_name`, `form_class`, and `success_url` attributes of the `RegisterView` class according to your project's setup.

Additionally, in your template (`register.html`), you can display the validation errors next to the corresponding form fields as shown in the previous response.


## List of fileds in User Model
The default User model provided by Django's authentication framework (`django.contrib.auth.models.User`) includes the following fields:

1. **username**: A unique identifier for the user. This field is required and must be unique.
2. **password**: A hashed password. This field stores the user's password securely.
3. **email**: The user's email address. This field is optional and can be used for communication or password recovery.
4. **first_name**: The user's first name.
5. **last_name**: The user's last name.
6. **is_staff**: A boolean field indicating whether the user has access to the admin site. By default, only superusers have staff status.
7. **is_active**: A boolean field indicating whether the user account is active. Inactive users cannot log in to the site.
8. **date_joined**: The date and time when the user account was created.

Additionally, Django's authentication framework provides methods and attributes for managing user authentication, permissions, and groups.

You can access the User model and its fields using the following import statement:

```python
from django.contrib.auth.models import User
```

You can also customize the User model or create a custom user model by subclassing `AbstractUser` or `AbstractBaseUser` provided by Django's authentication framework. This allows you to add or modify fields according to your application's requirements.

## password1 and password2
In Django's `UserCreationForm`, `password1` and `password2` are form fields used for collecting and confirming the user's password during registration.

Here's how they work:

- **password1**: This field is used to collect the user's chosen password.
- **password2**: This field is used to confirm the user's chosen password by asking them to enter it again.

When the form is submitted, Django's form validation ensures that the values entered in `password1` and `password2` match. If the values don't match, Django raises a validation error and prompts the user to enter the password again.

This password confirmation process helps prevent typos and ensures that the user enters their password correctly during registration.

Here's an example of how you can use `password1` and `password2` in a Django form:

```python
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'email']  # Include password1 and password2 fields in the form
```

In this form, `password1` and `password2` are included along with other fields such as username and email. When the form is rendered, `password1` is used to collect the user's chosen password, and `password2` is used to confirm it.

## Rendring errors in the form
To render form errors in a Django template, you can use the `{{ form.errors }}` template variable. This variable contains a dictionary of errors for each field in the form.

Here's how you can render form errors in your template:

```html
<!DOCTYPE html>
<html>
<head>
    <title>User Registration</title>
</head>
<body>
    <h2>User Registration</h2>
    <form method="post">
        {% csrf_token %}
        {{ form.as_p }}
        {% if form.errors %}
            <div class="alert alert-danger">
                <strong>Error:</strong> Please correct the following errors:<br>
                {% for field, errors in form.errors.items %}
                    {% for error in errors %}
                        {{ field }}: {{ error }}<br>
                    {% endfor %}
                {% endfor %}
            </div>
        {% endif %}
        <button type="submit">Register</button>
    </form>
</body>
</html>
```

In this example, we check if there are any errors in the form using `{% if form.errors %}`. If there are errors, we iterate over the `form.errors.items` dictionary to display each field name along with its corresponding error message.

Make sure to replace `'alert alert-danger'` with the appropriate CSS classes for styling the error message according to your project's design.

## Created user doing login
Once you have created a user using the registration form, you can use Django's built-in authentication views or handle the login process manually in your views. Here's how you can use Django's authentication views for login:

1. **Include Django's authentication URLs**: Make sure you include Django's authentication URLs in your project's `urls.py` file:

```python
from django.contrib.auth import views as auth_views

urlpatterns = [
    # Other URL patterns
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
]
```

2. **Redirect to login page after registration**: After a user successfully registers, you can redirect them to the login page:

```python
from django.shortcuts import redirect

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to login page after successful registration
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})
```

With this setup, after a user successfully registers, they will be redirected to the login page. They can then log in using the username and password they provided during registration.

Alternatively, if you want to handle the login process manually in your views, you can use Django's `authenticate` and `login` functions:

```python
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Redirect to home page after successful login
        else:
            # Invalid login
            # Handle invalid login error or render login page with error message
    # Render login page for GET request
    return render(request, 'login.html')
```

In this example, the `login_user` view handles the login process manually. After a user submits the login form, the view authenticates the user using the `authenticate` function and logs them in using the `login` function. If the login is successful, the user is redirected to the home page. Otherwise, an error message is displayed or the login page is rendered again with an error message.

Choose the approach that best fits your project's requirements and preferences.

## Using class
To implement login functionality using class-based views in Django, you can use `LoginView` provided by Django's authentication framework. Here's how you can do it using class-based views:

```python
from django.contrib.auth.views import LoginView

urlpatterns = [
    # Other URL patterns
    path('accounts/login/', LoginView.as_view(template_name='login.html'), name='login'),
]
```

In this URL configuration, we're using `LoginView` to handle the login process. We specify the template name as `'login.html'`, which is the template where the login form will be rendered.

Then, you need to create the login form template (`login.html`). Here's a simple example:

```html
<!DOCTYPE html>
<html>
<head>
    <title>Login</title>
</head>
<body>
    <h2>Login</h2>
    <form method="post">
        {% csrf_token %}
        {{ form.as_p }}
        <button type="submit">Login</button>
    </form>
</body>
</html>
```

This template renders the login form using `{{ form.as_p }}`, which renders each form field as a paragraph element. The form includes a CSRF token for security and a submit button for submitting the form.

With this setup, when a user accesses the `/accounts/login/` URL, they will be shown the login form. After entering their credentials and submitting the form, Django's authentication framework handles the authentication process and redirects the user accordingly.

You can customize the login form template (`login.html`) and add styling as needed to match your project's design.

## Restricting Acces to the App Functionality
Yes, you can restrict user access to certain functionality or views in Django by using decorators or mixins that check if the user is authenticated. Here's how you can do it:

1. **Using `login_required` decorator**: You can use the `login_required` decorator provided by Django to restrict access to views that require authentication. Import it from `django.contrib.auth.decorators` and apply it to your views like this:

```python
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required
def my_protected_view(request):
    # View logic for authenticated users
    return render(request, 'my_protected_view.html')
```

In this example, the `my_protected_view` function-based view can only be accessed by authenticated users. If an unauthenticated user tries to access this view, they will be redirected to the login page.

2. **Using `LoginRequiredMixin`**: If you're using class-based views, you can use Django's `LoginRequiredMixin` to achieve the same behavior. Import it from `django.contrib.auth.mixins` and include it in your view class:

```python
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

class MyProtectedView(LoginRequiredMixin, TemplateView):
    template_name = 'my_protected_view.html'
```

In this example, the `MyProtectedView` class-based view requires the user to be authenticated. If an unauthenticated user tries to access this view, they will be redirected to the login page.

By using either the `login_required` decorator or `LoginRequiredMixin`, you can ensure that certain functionality in your Django application is only accessible to authenticated users.

## Implementing logoff function
To implement a log-off (logout) function in your Django application, you can use Django's `LogoutView` provided by the authentication framework. Here's how you can do it:

1. **URL Configuration**: Include Django's `LogoutView` in your URL configuration to handle the logout process:

```python
from django.contrib.auth.views import LogoutView

urlpatterns = [
    # Other URL patterns
    path('accounts/logout/', LogoutView.as_view(), name='logout'),
]
```

2. **Logout Link**: In your template, provide a link to the logout URL so users can initiate the logout process:

```html
<!DOCTYPE html>
<html>
<head>
    <title>My App</title>
</head>
<body>
    <h2>Welcome, {{ request.user.username }}</h2>
    <a href="{% url 'logout' %}">Logout</a>
</body>
</html>
```

In this example, `{{ request.user.username }}` is used to display the currently logged-in user's username, and the "Logout" link points to the URL mapped to the `LogoutView`.

With this setup, when a user clicks the "Logout" link, Django's `LogoutView` will handle the logout process. The user will be logged out and redirected to the login page by default.

You can customize the logout behavior by providing a `next_page` parameter to the `LogoutView` in your URL configuration. For example:

```python
path('accounts/logout/', LogoutView.as_view(next_page='/accounts/login/'), name='logout'),
```

In this case, after logout, the user will be redirected to the login page specified by `next_page`. Adjust the URL as needed based on your project's URL structure.

## log in and logoff in view
To create a view file for your logout functionality in Django, you typically don't need to create a separate view file if you're using Django's built-in authentication views. However, you can organize your views in a separate file if you prefer. Here's how you can do it:

1. Create a new Python file for your views, for example, `views.py`, in your Django app directory if you don't already have one.

2. Define your views in this file. Since you're using Django's built-in authentication views, you don't need to define a view for logout. However, you can define other views here if needed.

```python
# views.py
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic import TemplateView

class MyLoginView(LoginView):
    template_name = 'login.html'

class MyLogoutView(LogoutView):
    next_page = reverse_lazy('login')

class MyProtectedView(TemplateView):
    template_name = 'my_protected_view.html'
```

In this example, `MyLoginView` and `MyLogoutView` are subclasses of Django's built-in authentication views `LoginView` and `LogoutView`, respectively. You can customize them as needed, such as specifying the template name or the URL to redirect to after logout.

3. Use these views in your URL configuration as previously shown. Make sure to import them from your `views.py` file.

```python
# urls.py
from django.urls import path
from .views import MyLoginView, MyLogoutView, MyProtectedView

urlpatterns = [
    path('accounts/login/', MyLoginView.as_view(), name='login'),
    path('accounts/logout/', MyLogoutView.as_view(), name='logout'),
    # Other URL patterns
]
```

With this setup, you have organized your views in a separate file (`views.py`) and can use them in your URL configuration. Make sure to adjust the import paths and view names according to your project's structure.

## Login required to access Class views
To make a class-based view require login in Django, you can use Django's `LoginRequiredMixin`. This mixin ensures that only authenticated users can access the view. Here's how to use it:

```python
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

class MyProtectedView(LoginRequiredMixin, TemplateView):
    template_name = 'my_protected_view.html'
```

In this example, `MyProtectedView` is a class-based view that requires the user to be authenticated. If an unauthenticated user tries to access this view, they will be redirected to the login page.

You can customize the behavior of the `LoginRequiredMixin` by specifying additional parameters. For example, you can set the `login_url` attribute to specify a custom URL to redirect to for login:

```python
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

class MyProtectedView(LoginRequiredMixin, TemplateView):
    template_name = 'my_protected_view.html'
    login_url = '/accounts/login/'  # Custom login URL
```

With this setup, when an unauthenticated user tries to access `MyProtectedView`, they will be redirected to the custom login URL specified by `login_url`.

Make sure to adjust the view class name and template name according to your project's structure and requirements.

## getting login user in class (view)
To access the currently logged-in user's username in a class-based view, you can use `self.request.user.username`. Here's how you can do it in a `CreateView`:

```python
from django.views.generic import CreateView
from yourapp.models import YourModel

class YourCreateView(CreateView):
    model = YourModel
    fields = ['field1', 'field2']  # Specify the fields of YourModel that you want to include in the form
    template_name = 'your_template.html'
    success_url = '/success/'  # Specify the URL to redirect to after successful form submission

    def form_valid(self, form):
        form.instance.user = self.request.user  # Assign the currently logged-in user to the 'user' field of the instance being created
        return super().form_valid(form)
```

In this example, `form.instance.user` refers to the user field of the model instance being created by the form. By setting it to `self.request.user`, you assign the currently logged-in user to this field.

Make sure your model (`YourModel` in this example) has a `user` field to store the username. Adjust the field name accordingly if it's different in your model.

Now, when a user submits the form, the currently logged-in user's username will be assigned to the appropriate field of the newly created instance.

## Adding values to Forms before saving
If you don't want to render the `created_by` field in the form for the user to see or interact with, you can exclude it from the form fields and set its value in the view before saving the form. Here's how you can do it:

```python
from django.views.generic import CreateView
from yourapp.models import YourModel

class YourCreateView(CreateView):
    model = YourModel
    fields = ['field1', 'field2']  # Exclude 'created_by' field from the form
    template_name = 'your_template.html'
    success_url = '/success/'  # Specify the URL to redirect to after successful form submission

    def form_valid(self, form):
        form.instance.created_by = self.request.user  # Assign the currently logged-in user to the 'created_by' field of the instance being created
        return super().form_valid(form)
```

In this example, I've removed `'created_by'` from the `fields` attribute of the view, so it won't be rendered in the form. Then, in the `form_valid` method, I'm setting the `created_by` field value manually to the currently logged-in user.

This way, the `created_by` field will still be set to the logged-in user when the form is submitted, but it won't be visible or editable by the user in the form.
