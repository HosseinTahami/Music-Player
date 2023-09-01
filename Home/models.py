from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=128)
    info = models.TextField()
    genre_img = models.ImageField()

    def __str__(self) -> str:
        return f"Name: {self.name}"


class Song(models.Model):
    name = models.CharField(max_length="128")
    cover_img = models.ImageField("song_cover_images/")
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    audio_file = models.FieldFile(upload_to="song_files/")
    genres = models.ManyToManyField(Genre)
    # artist =

    def __str__(self) -> str:
        return f"id: {self.id} || name: {self.name}"
