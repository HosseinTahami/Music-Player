# Django Imports
from django.shortcuts import render, redirect, HttpResponse
from django.views import View
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.hashers import make_password
from django.core.exceptions import ObjectDoesNotExist

# Inside Project Imports
from .forms import RegisterForm, LoginForm, ArtistProfileForm, ListenerProfileForm
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
                    username=cd["username"],
                    email=cd["email"],
                    password=make_password(cd["password"]),
                )
                ns(request, "Register as Listener User Successfully", "success")
            else:
                Artist.objects.create(
                    username=cd["username"],
                    email=cd["email"],
                    password=make_password(cd["password"]),
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
                request, username=cd["username_email"], password=cd["password"]
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


# class ProfileView(LoginRequiredMixin, View):
#     def get(self, request, *args, **kwargs):
#         if Artist.objects.get(username=self.request.user.username):
#             user = Artist.objects.get(username=self.request.user.username)
#             context = {"form": ArtistProfileForm(instance=user)}
#         if Listener.objects.get(username=self.request.user):
#             user = Listener.objects.get(username=self.request.user.username)
#             context = {"form": ListenerProfileForm(instance=user)}
#         return render("accounts/profile.html", context)

#     def post(self, request, *args, **kwargs):
#         if Artist.objects.get(username=self.request.user.username):
#             form = ArtistProfileForm(request.POST)
#         if Listener.objects.get(username=self.request.user.username):
#             form = ArtistProfileForm(request.POST)
#         if form.is_valid:
#             form.save()


class ProfileView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        try:
            user = Artist.objects.get(username=self.request.user.username)
            context = {"form": ArtistProfileForm(instance=user), "user": user}
        except ObjectDoesNotExist:
            try:
                user = Listener.objects.get(username=self.request.user.username)
                context = {"form": ListenerProfileForm(instance=user), "user": user}
            except ObjectDoesNotExist:
                return HttpResponse("User profile not found")

        return render(request, "accounts/profile.html", context)

    def post(self, request, *args, **kwargs):
        try:
            user = Artist.objects.get(username=self.request.user.username)
            form = ArtistProfileForm(request.POST, instance=user)
        except ObjectDoesNotExist:
            try:
                user = Listener.objects.get(username=self.request.user.username)
                form = ListenerProfileForm(request.POST, instance=user)
            except ObjectDoesNotExist:
                return HttpResponse("User profile not found")

        if form.is_valid:
            form.save()
            return HttpResponse("Good")
        else:
            context = {"form": form}
            return render(request, "accounts/profile.html", context)


class ArtistsView(ListView):
    template_name = "accounts/artists.html"
    model = Artist
    context_object_name = "artists"
    queryset = Artist.objects.all()
