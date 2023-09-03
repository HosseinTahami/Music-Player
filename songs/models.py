# Django Imports
from django.db import models

# Inside Imports


class Genre(models.Model):
    name = models.CharField(max_length=128, unique=True)
    info = models.TextField(default=True)
    genre_img = models.ImageField()

    def __str__(self) -> str:
        return f"Name: {self.name}"


class Song(models.Model):
    title = models.CharField(max_length=60)
    cover_img = models.ImageField("songs/images/SongCover/")
    description = models.TextField(default=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    audio_file = models.FileField(upload_to="songs/audio/")
    genres = models.ManyToManyField(Genre)
    band = models.ForeignKey(
        "accounts.Band", on_delete=models.PROTECT, null=True, blank=True
    )
    artist = models.ManyToManyField("accounts.Artist")

    def __str__(self) -> str:
        return f"id: {self.id} || title: {self.title}"
