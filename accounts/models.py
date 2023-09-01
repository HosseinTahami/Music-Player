"""
In the Next Version I should Create an CustomAbstractBaseUserManager
then Artist & Listener will inheritance it !
 
"""

from django.db import models
from django.contrib.auth.models import AbstractBaseUser


class Artist(AbstractBaseUser):
    username = models.CharField(max_length=28, unique=True)
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    email = models.EmailField(unique=True)
    gender = models.BooleanField(default=True)
    bio = models.TextField(blank=True, null=True)
    profile_img = models.ImageField(upload_to="artists_images/")
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_alive = models.BooleanField(default=True)

    USERNAME_FIELD = [
        "username",
        "email",
    ]

    def __str__(self) -> str:
        return f"Name: {self.first_name} {self.last_name} || Email:{self.email}"


class Listener(AbstractBaseUser):
    username = models.CharField(max_length=28, unique=True)
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    email = models.EmailField(unique=True)
    gender = models.BooleanField(default=True)
    bio = models.TextField(blank=True, null=True)
    profile_img = models.ImageField(upload_to="listeners_images/")

    USERNAME_FIELD = [
        "username",
        "email",
    ]

    def __str__(self) -> str:
        return f"Name: {self.first_name} {self.last}"
