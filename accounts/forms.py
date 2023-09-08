# Django Imports
from django import forms


# Inside Project Imports
from .models import Listener, Artist


class RegisterForm(forms.Form):
    USER_TYPE_CHOICES = [
        ("Artist", "Artist"),
        ("Listener", "Listener"),
    ]
    user_type = forms.ChoiceField(
        choices=USER_TYPE_CHOICES,
        widget=forms.Select(
            attrs={
                "placeholder": "User Type",
                "class": "form-select m-3",
            }
        ),
    )

    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Username",
                "class": "form-control form-control-lg m-3",
            }
        )
    )

    email = forms.EmailField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Example@email.com",
                "class": "form-control form-control-lg m-3",
            }
        )
    )

    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Password",
                "class": "form-control form-control-lg m-3",
            }
        )
    )

    confirm_password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Confirm Password",
                "class": "form-control form-control-lg m-3",
            }
        )
    )


class LoginForm(forms.Form):
    username_email = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "label": "Username or Email",
                "placeholder": "Enter your email or username",
                "class": "form-control form-control-lg m-3",
            }
        )
    )

    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Password",
                "class": "form-control form-control-lg m-3",
            }
        )
    )

    remember_me = forms.BooleanField(required=False)


class ArtistProfileForm(forms.ModelForm):
    class Meta:
        model = Artist
        fields = [
            "first_name",
            "last_name",
            "band",
            "gender",
            "profile_img",
            "email",
            "username",
            "bio",
        ]


class ListenerProfileForm(forms.ModelForm):
    class Meta:
        model = Listener
        fields = [
            "first_name",
            "last_name",
            "gender",
            "profile_img",
            "email",
            "username",
        ]
