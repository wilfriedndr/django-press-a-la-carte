from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login


def my_view(request):
    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        # Redirect to a success page.
        return "login successful"
    else:
        # Return an 'invalid login' error message.
        return "login unsuccessful"

class RegisterForm(UserCreationForm):
    class Meta:
        model=User
        fields = ['username','email','password'] 