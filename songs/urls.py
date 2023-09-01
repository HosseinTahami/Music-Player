from django.urls import path
from . import views

app_name = "songs"

urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
]
