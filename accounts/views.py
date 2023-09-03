# Django Imports
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login, logout, authenticate

# Inside Project Imports
from .forms import RegisterForm, LoginForm
from .models import Listener, Artist
from .utils import notification_system as ns


class RegisterView(View):
    form_class = RegisterForm
    template_name = "accounts/register.html"

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect("songs:home")
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        # ns(request, "went to Register page", "success")
        return render(request, self.template_name, {"form": form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            if cd["user_type"] == "Listener":
                Listener.objects.create(
                    username=cd["username"], email=cd["email"], password=cd["password"]
                )
                ns(request, "Register as Listener User Successfully", "success")
            else:
                Artist.objects.create(
                    username=cd["username"], email=cd["email"], password=cd["password"]
                )
        return redirect("songs:home")


class LoginView(View):
    form_class = LoginForm
    template_name = "accounts/login.html"

    def get(self, request):
        form = self.form_class
        return render(request, self.template_name, {"form": form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            print("----------form is valid-----------")
            cd = form.cleaned_data

            user_1 = authenticate(
                request, email=cd["username_email"], password=cd["password"]
            )
            user_2 = authenticate(
                request, username=cd["username_email"], password=cd["password"]
            )
            if user_1 != None:
                print("-----Email-----------")
                login(request, user_1)
                return redirect("songs:home")
            elif user_2 != None:
                print("-------Username----------")
                login(request, user_2)
                return redirect("songs:home")
        print("----------None-----------")
        print(cd["username_email"])
        print(cd["password"])
        return render(request, self.template_name, {"form": form})


class LogoutView(LoginRequiredMixin, View):
    def get(self, request):
        logout(request)
        ns(request, "Logout Successfully", "success")
        return redirect("accounts:login")


class ProfileView(View):
    pass
