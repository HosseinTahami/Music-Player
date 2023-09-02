# Django Imports
from django.urls import path

# Inside Project Imports
from . import views

app_name = "accounts"

urlpatterns = [path("login/", views.SignUpView.as_view(), name="login")]
