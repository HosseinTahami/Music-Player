from django.urls import path
from . import views

app_name = "songs"

urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path("genres/", views.GenreListView.as_view(), name="genres"),
    path("songs/", views.SongListView.as_view(), name="songs"),
]
