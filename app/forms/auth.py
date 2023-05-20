from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login


def LoginForm(request):
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

def RegistrationForm(request):
    username = request.POST["username"]
    password = request.POST["password"]
    email = request.POST["email"]
    user = authenticate(request, username=username, password=password, email=email)
    if user is not None:
        login(request, user)
        # Redirect to a success page.
        return "regitration successful"
    else:
        # Return an 'invalid login' error message.
        return "registration unsuccessful"