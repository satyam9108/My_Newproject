from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import UserManager
# Create your models here.

class User(AbstractUser):
    ROLE_CHOICES = [
        ('planner', 'Planner'),
        ('teacher', 'Teacher'),
    ]
    username=None
    email=models.EmailField(unique=True,null=True,blank=True)
    role=models.CharField(max_length=100,choices= ROLE_CHOICES,null=True,blank=True)
    last_login_time=models.DateTimeField(null=True,blank=True)
    last_logout_time=models.DateTimeField(null=True,blank=True)

    objects=UserManager()

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS =[]

