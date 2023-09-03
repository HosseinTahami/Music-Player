# Django Imports
from django.urls import path

# Inside Project Imports
from . import views

app_name = "accounts"

urlpatterns = [
    path("register/", views.RegisterView.as_view(), name="register"),
    path("login/", views.LoginView.as_view(), name="login"),
    path("logout/", views.LogoutView.as_view(), name="logout"),
    path("profile/<int:pk>", views.ProfileView.as_view(), name="profile"),
    path("artists/", views.ArtistsView.as_view(), name="artist"),
]
