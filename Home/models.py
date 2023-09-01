from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=128)
    info = models.TextField()
    genre_img = models.ImageField()

    def __str__(self) -> str:
        return f"Name: {self.name}"
