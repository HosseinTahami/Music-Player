"""
In the Next Version I should Create an CustomAbstractBaseUser
then Artist & Listener will inheritance it !
 
"""
# Django Imports
from django.db import models
from django.contrib.auth.models import AbstractBaseUser

# Inside Project Imports


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


class Band(models.Model):
    name = models.CharField(max_length=128)
    started_at = models.DateTimeField()
    end_at = models.DateTimeField()


class Artist(CustomAbstractBaseUser):
    from songs.models import Song

    songs = models.ManyToManyField(Song)
    band = models.ForeignKey(Band)
    profile_img = models.ImageField(upload_to="accounts/artist_images/")


class Listener(CustomAbstractBaseUser):
    is_premium = models.BooleanField(default=False)
    profile_img = models.ImageField(upload_to="accounts/listener_images/")
