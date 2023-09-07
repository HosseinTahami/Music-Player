# Django Imports
from django import forms

# Inside Project Imports
from .models import Playlist


class CreatePlayListForm(forms.ModelForm):
    model = Playlist

    class Meta:
        fields = "__all__"
