from django.contrib.auth.models import AbstractUser
from django.db import models
from django.forms import CharField


# Create your models here.

class Login(AbstractUser):
    is_customer = models.BooleanField(default=False)
    is_worker = models.BooleanField(default=False)


class Register(models.Model):
    user = models.OneToOneField(Login, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=1000)
    mobile = models.CharField(max_length=40)
    email = models.EmailField()
