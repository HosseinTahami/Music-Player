# Django Imports
from django.db import models
from django.contrib.auth.models import PermissionsMixin, AbstractBaseUser


# Inside Project Imports
from .managers import CustomUserManager


class BaseUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=28, unique=True)
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    email = models.EmailField(unique=True)
    gender = models.BooleanField(default=True)
    bio = models.TextField(blank=True, null=True)
    created_at = models.DateField(auto_now_add=True, editable=True)
    updated_at = models.DateTimeField(auto_now=True, editable=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]
    objects = CustomUserManager()

    def __str__(self) -> str:
        return f"Name: {self.first_name} {self.last_name} || Email:{self.email}"


class Listener(BaseUser):
    USER_TYPE_CHOICES = (
        ("F", "Free"),
        ("P", "Premium"),
    )
    user_type = models.CharField(max_length=1, choices=USER_TYPE_CHOICES, default="F")
    profile_img = models.ImageField(
        upload_to="accounts/images/Listener/",
        default="accounts/images/Listener/default.png",
    )
    premium_left = models.IntegerField(default=0)


class Artist(BaseUser):
    band = models.ForeignKey("Band", on_delete=models.PROTECT, blank=True, null=True)
    profile_img = models.ImageField(
        upload_to="accounts/images/Artist", default="accounts/images/Artist/default.png"
    )


class Band(models.Model):
    name = models.CharField(max_length=128)
    started_at = models.DateTimeField(auto_now_add=True, editable=False)
    end_at = models.DateTimeField(null=True, blank=True, editable=True)

    def __str__(self) -> str:
        return f"Name: {self.name}"
