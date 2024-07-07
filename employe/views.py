from .models import *
from django.contrib import auth
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .form import *
# home page
def home(request):
    return render(request, "home.html")

def base(request):
    return render(request, "base.html")

#login page 
def login_employe(request):
    if request.method == 'POST':
        username = request.POST.get('login')
        password = request.POST.get('pass')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("employe:base")
        else:
            messages.warning(request, 'something went wrong')
            return redirect('employe:login')
    return render(request,'login.html')


