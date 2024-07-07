from .models import *
from django.contrib import auth
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .form import *
from employe.models import Client
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

#add client
from django.shortcuts import render, redirect
from django.contrib import messages
from django.db import IntegrityError
from .models import Client

def ADD_CLIENT(request):
    if request.method == 'POST':
        id = request.POST.get('client_id')
        name = request.POST.get('client_name')
        birth = request.POST.get('client_birth')
        phone = request.POST.get('client_phone')
        email = request.POST.get('client_email')
        gender = request.POST.get('client_gender')
        address = request.POST.get('client_Address')

        if not all([id, name, birth, phone, email, gender, address]):
            messages.error(request, 'All fields are required.')
            return render(request, 'client/add_client.html')

        client = Client(
            client_id=id,
            client_Name=name,
            Date_Of_Birth=birth,
            Phone=phone,
            Email=email,
            Gender=gender,
            Address=address,
        )

        try:
            client.save()
            messages.success(request, 'Client added successfully!')
            return redirect('employe:add_client')
        except IntegrityError:
            messages.error(request, 'Client ID already exists.')
            return render(request, 'client/add_client.html')

    return render(request, 'client/add_client.html')



#add operation
from django.shortcuts import render, redirect
from .form import OperationForm

from django.shortcuts import render, redirect
from django.db import IntegrityError
from django.contrib import messages
from .form import OperationForm

def ADD_OPERATION(request):
    if request.method == 'POST':
        form = OperationForm(request.POST, request.FILES)
        try:
            if form.is_valid():
                form.save()
                messages.success(request, 'Operation added successfully!')
                return redirect('employe:add_operation')
        except IntegrityError:
            messages.error(request, 'Operation ID already exists.')
            return render(request, 'client/add_operation.html', {'form': form})
    else:
        form = OperationForm()  # Ensure form is initialized for GET request

    return render(request, 'client/add_operation.html', {'form': form})
