from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    username = None
    first_name = models.CharField(max_length=100) 
    last_name = models.CharField(max_length=100) 
    address = models.TextField(max_length=200)
    email = models.EmailField(unique=True)
    phone_number = models.IntegerField(null=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email
    