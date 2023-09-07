# Django Imports
from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import CreateView, ListView, DeleteView
from django.urls import reverse_lazy

# Inside Project Imports
from .models import Playlist
from accounts.models import BaseUser


class CreatePlaylistView(CreateView):
    model = Playlist
    fields = ["name", "cover_img", "description", "songs"]
    template_name = "interactions/create_playlist.html"
    success_url = reverse_lazy("songs:home")

    def form_valid(self, form):
        playlist = form.save(commit=False)
        print(self.request.user.username)
        playlist.owner = BaseUser.objects.get(username=self.request.user.username)
        playlist.save()
        return super().form_valid(form)


class PlaylistView(ListView):
    model = Playlist
    queryset = Playlist.objects.all()
    context_object_name = "playlists"
    template_name = "interactions/playlists.html"


class YourPlaylistView(ListView):
    model = Playlist
    context_object_name = "playlists"
    template_name = "interactions/your_playlists.html"

    def get_queryset(self):
        return Playlist.objects.filter(owner=self.request.user)


class DeletePlaylistView(DeleteView):
    model = Playlist
    success_url = reverse_lazy("interactions:playlists")
    template_name = "interactions/delete_playlist.html"
