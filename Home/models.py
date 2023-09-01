from django.db import models

from accounts.models import Listener


class Genre(models.Model):
    name = models.CharField(max_length=128, unique=True)
    info = models.TextField(default=True)
    genre_img = models.ImageField()

    def __str__(self) -> str:
        return f"Name: {self.name}"


class Song(models.Model):
    name = models.CharField(max_length="128")
    cover_img = models.ImageField("song_cover_images/")
    description = models.TextField(default=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    audio_file = models.FieldFile(upload_to="song_files/")
    genres = models.ManyToManyField(Genre)

    def __str__(self) -> str:
        return f"id: {self.id} || name: {self.name}"


class Playlist(models.Model):
    name = models.CharField(max_length=128)
    cover_img = models.ImageField(upload_to="playlist_cover_images/")
    description = models.TextField(default=True, null=True)
    songs = models.ManyToManyField(Song)
    created_at = models.DateField(auto_now_add=True)
    owner = models.ForeignKey(Listener)

    def __str__(self) -> str:
        return f"Name: {self.name}"
