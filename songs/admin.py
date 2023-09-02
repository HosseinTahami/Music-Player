# Django Imports
from django.contrib import admin

# Inside Project Imports
from .models import Genre, Song

admin.site.register(Genre)
admin.site.register(Song)
