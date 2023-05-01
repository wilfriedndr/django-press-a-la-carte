from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.http import HttpResponseNotFound, HttpResponseRedirect
from .forms import SubscriptionForm, SubscriberForm, RegisterForm, LoginForm
from .models import Subscriber, UserExists, User
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
"""
def create_user(request, *args, **kwargs):
    # Do some parameter validation
    try:
        User.objects.create_user(User.username, User.email, User.password)
    except UserExists:
        return HttpResponseNotFound("<h1>User exists</h1>")
    return HttpResponse("<h1>User created!</h1>")
"""
def index(request):
    return render(request, 'base.html', {})

def subscription(request):
    return render(request, 'subscription_form.html', {})

def login(request):
    return render(request, 'login_form.html',  {})

def register(request):
    return render(request, 'register_form.html', {})
"""
def LoginForm(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        email = request.POST["email"]
        user = authenticate(request, username=username, email=email, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            return HttpResponseRedirect('/')
        else:
            # Return an 'invalid login' error message.
            return HttpResponseRedirect('login')

def SubscriptionForm(request):
    if request.method == 'POST':
        subscriber_form  = SubscriberForm(request.POST)
        subscription_form = SubscriptionForm(request.POST)
        if subscriber_form.is_valid() and subscription_form.is_valid():
            subscriber = subscriber_form.save()
            subscription.save(email=subscriber.email)
            return HttpResponseRedirect('/thanks/')
    return render(request, 'base.html', {'subscriber_form': subscriber_form, 'subscription_form':subscription_form})

@csrf_exempt
def register_form(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('home')
        else:
            print(form.error)
            print(form.errors.as_data())
        return render(request, 'base.html', { 'form': form})
"""    


"""
def SubscriptionForm(request):
    if request.method == 'POST':
        form = SubscriptionForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            address = form.cleaned_data['address']
            age = form.cleaned_data['age']
            rubrics = form.cleaned_data['rubrics']
            form.save()
            print(form)
            return render(request, 'base.html', {form: form})
    else:
        print('no go')
        form = SubscriptionForm()
    return render(request, 'base.html', {})
    """