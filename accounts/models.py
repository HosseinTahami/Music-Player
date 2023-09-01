"""
In the Next Version I should Create an CustomAbstractBaseUser
then Artist & Listener will inheritance it !
 
"""
# Django Imports
from django.db import models
from django.contrib.auth.models import AbstractBaseUser

# Inside Project Imports
from songs.models import Song


class CustomAbstractBaseUser(AbstractBaseUser):
    username = models.CharField(max_length=28, unique=True)
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    email = models.EmailField(unique=True)
    gender = models.BooleanField(default=True)
    bio = models.TextField(blank=True, null=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name"]

    def __str__(self) -> str:
        return f"Name: {self.first_name} {self.last_name} || Email:{self.email}"


class Listener(CustomAbstractBaseUser):
    USER_TYPE_CHOICES = (
        ("F", "Free"),
        ("P", "Premium"),
    )
    user_type = models.CharField(max_length=1, choices=USER_TYPE_CHOICES, default="F")
    profile_img = models.ImageField(upload_to="accounts/ListenerImages/")


class Artist(CustomAbstractBaseUser):
    songs = models.ManyToManyField(Song)
    band = models.ForeignKey("Band", on_delete=models.PROTECT)
    profile_img = models.ImageField(upload_to="accounts/ArtistImages/")


class Band(models.Model):
    name = models.CharField(max_length=128)
    started_at = models.DateTimeField()
    end_at = models.DateTimeField()
