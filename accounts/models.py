from django.db import models
from django.contrib.auth.models import AbstractBaseUser


class Artist(AbstractBaseUser):
    username = models.CharField(max_length=28, unique=True)
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    email = models.EmailField()
    gender = models.BooleanField()
    bio = models.CharField(max_length=128)
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
