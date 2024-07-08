from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views
from .views import Clients_show, Generate_pdf

app_name = "employe"

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_employe, name='login'),
    path('base/', views.base, name='base'),
    path('client/add',views.ADD_CLIENT,name='add_client'),
    path('operation/add',views.ADD_OPERATION,name='add_operation'),
    path('client/show', Clients_show.as_view(), name='client_show'),
    path('clients/<str:client_id>/pdf/', views.Generate_pdf, name='generate_pdf'),

]