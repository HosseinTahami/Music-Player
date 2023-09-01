from django.db import models

from accounts.models import Listener
from songs.models import Song


class Playlist(models.Model):
    name = models.CharField(max_length=128)
    cover_img = models.ImageField(upload_to="playlist_cover_images/")
    description = models.TextField(default=True, null=True)
    songs = models.ManyToManyField(Song)
    created_at = models.DateField(auto_now_add=True)
    owner = models.ForeignKey(Listener)

    def __str__(self) -> str:
        return f"Name: {self.name}"


class Like(models.Model):
    song = models.ForeignKey(Song)
    liker = models.ForeignKey(Listener)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"Name: {self.name}"


class comment(models.Model):
    song = models.ForeignKey(Song)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"Name: {self.name}"
