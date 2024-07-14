from django.contrib.auth.models import User
from django.db import models

class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Add other fields as needed
from django.utils import timezone


class Client(models.Model):
    client_id=models.CharField(max_length=100,editable=False, unique=True)
    client_Name=models.CharField(max_length=100)
    Date_Of_Birth=models.CharField(max_length=100)
    created_date = models.DateField(default=timezone.now)
    Phone=models.IntegerField()
    Email=models.CharField(max_length=100)
    Gender=models.CharField(max_length=100)
    Address=models.TextField()

    def __str__(self):
        return self.client_id
    



class Operation(models.Model):
    client_id = models.CharField(max_length=100)
    operation = models.CharField(max_length=100)
    operation_date = models.DateField(default=timezone.now)
    observation = models.TextField()
    piece_jointe = models.FileField(upload_to='piece_jointe/')
    confirmed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.client_id} - {self.operation}"
