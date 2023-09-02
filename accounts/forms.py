# Django Imports
from django import forms

# Inside Project Imports
from .models import Listener, Artist


class RegisterForm(forms.ModelForm):
    USER_TYPE_CHOICES = [
        ("Artist", "A"),
        ("Listener", "L"),
    ]
    user_type = forms.ChoiceField(
        choices=USER_TYPE_CHOICES,
        widget=forms.RadioSelect(
            attrs={
                "placeholder": "User Type",
                "class": "form-control",
            }
        ),
    )
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Confirm Password",
                "class": "form-control",
            }
        )
    )

    class Meta:
        model = Listener
        fields = (
            "email",
            "username",
            "password",
        )
