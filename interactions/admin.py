# Django Imports
from django.contrib import admin

# Inside Project Imports
from .models import Like, comment, Playlist

admin.site.register(Like)
admin.site.register(comment)
admin.site.register(Playlist)
