from django.db import models
from django.contrib.auth.models import User,AbstractBaseUser, BaseUserManager, PermissionsMixin

class employe(models.Model):
    email = models.EmailField(primary_key=True)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.email