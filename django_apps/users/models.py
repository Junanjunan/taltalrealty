from django.db import models
from django.contrib.auth.models import AbstractUser
from .login_type import LOGIN_CHOICES


class User(AbstractUser):
    login_method = models.CharField(max_length=50, choices=LOGIN_CHOICES, default="email")


class Office(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=150)
    phone = models.CharField(max_length=30)
    fax = models.CharField(max_length=30, null=True, blank=True)

    def __str__(self):
        return self.name
    

class Realtor(models.Model):
    name = models.CharField(max_length=20)
    account = models.ForeignKey("User", on_delete=models.CASCADE)
    office = models.ForeignKey("Office", on_delete=models.DO_NOTHING, null=True, blank=True)
    is_owner = models.BooleanField()
    phone = models.CharField(max_length=30, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    introduction = models.TextField(blank=True)

    def __str__(self):
        return self.name
    

