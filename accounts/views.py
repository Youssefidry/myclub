# accounts/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from .forms import RegistrationForm
from django.contrib.auth.models import User


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Replace 'home' with the URL name of your homepage
        else:
            # Handle invalid login
            return render(request, 'accounts/login.html', {'error': 'Invalid login credentials.'})
    else:
        return render(request, 'accounts/login.html')

def logout_view(request):
    logout(request)
    return redirect('login')  # Replace 'login' with the URL name of your login page

def signout_view(request):
    return HttpResponse("This is a sign out view.")

def register_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            User.objects.create_user(username=username, email=email, password=password)
            return redirect('login')  # Replace 'login' with the URL name for your login page
    else:
        form = RegistrationForm()
    return render(request, 'accounts/register.html', {'form': form})
