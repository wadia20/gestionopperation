from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

app_name = "employe"

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_employe, name='login'),
    path('base/', views.base, name='base') 
    
]