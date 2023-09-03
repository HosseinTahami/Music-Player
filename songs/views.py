# Django Imports
from django.shortcuts import render
from django.views import View
from django.views.generic import DetailView, ListView

# Inside Project Imports
from .models import Genre, Song


class HomeView(View):
    def get(self, request):
        return render(request, "songs/home.html")


class GenreListView(ListView):
    template_name = "songs/genres.html"
    model = Genre
    context_object_name = "genres"
    queryset = Genre.objects.all()


class GenreDetailView(DetailView):
    pass


class SongListView(ListView):
    template_name = "songs/songs.html"
    model = Genre
    context_object_name = "songs"
    queryset = Song.objects.all()
