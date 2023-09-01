from django.contrib.auth.models import BaseUserManager
from django.core.exceptions import ValidationError


class ArtistManager(BaseUserManager):
    def create_user(
        self, first_name, last_name, username, email, bio, gender, profile_img, is_alive
    ):
        if not first_name:
            raise ValidationError("Artist Users Should Have First Name.")
        if not last_name:
            raise ValidationError("Artist Users Should Have Last Name.")
        if not (username or email):
            raise ValidationError("Artist Users Should Have an Email or Username")

        artist = self.model(
            first_name=first_name,
            last_name=last_name,
            username=username,
            email=email,
            is_alive=is_alive,
            profile_img=profile_img,
            bio=bio,
            gender=gender,
        )

        artist.set_password()
        artist.save(using=self._db)
        return artist
