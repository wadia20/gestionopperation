from django.contrib.auth.models import User
from django.db import models

class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Add other fields as needed


class Client(models.Model):
    client_id=models.CharField(max_length=100,editable=False, unique=True)
    client_Name=models.CharField(max_length=100)
    Date_Of_Birth=models.CharField(max_length=100)
    Phone=models.IntegerField()
    Email=models.CharField(max_length=100)
    Gender=models.CharField(max_length=100)
    Address=models.TextField()

    def __str__(self):
        return self.client_id