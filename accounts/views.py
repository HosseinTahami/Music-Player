# Django Imports
from django.shortcuts import render, redirect
from django.views import View

# Inside Project Imports
from .forms import RegisterForm
from .models import Listener, Artist


class RegisterView(View):
    form_class = RegisterForm
    template_name = "accounts/register.html"

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect("songs:home")
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {"form": form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid:
            cd = form.cleaned_data
        if cd["user_type"] == "L":
            Listener.objects.create(
                username=cd["username"], email=cd["email"], password=cd["password"]
            )
        else:
            Artist.objects.create(
                username=cd["username"], email=cd["email"], password=cd["password"]
            )
        return redirect("songs:home")
