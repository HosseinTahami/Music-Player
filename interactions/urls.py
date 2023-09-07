# Django imports
from django.urls import path

# Inside Project imports
from . import views

app_name = "interactions"

urlpatterns = [
    path(
        "playlist/create/",
        views.CreatePlaylistView.as_view(),
        name="create_playlist",
    ),
    path(
        "playlists/",
        views.PlaylistView.as_view(),
        name="playlists",
    ),
    path(
        "playlist/delete/<int:pk>",
        views.DeletePlaylistView.as_view(),
        name="delete_playlist",
    ),
    path("your/playlists/", views.YourPlaylistView.as_view(), name="your_playlists"),
]
