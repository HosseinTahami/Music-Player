from accounts.models import BaseUser as User
from django.contrib.auth.backends import ModelBackend


class EmailOrUsernameAuthenticationBackend(ModelBackend):
    """
    The reason we are using try and except block is because when there is no user with that
    email address or with that user id, the user variable will not become equal to None but
    an Error named User Does Not Exist will be raised.
    """

    def authenticate(self, request, username=None, password=None):
        try:
            user = User.objects.get(email=username)
            print("authenticate:", username)

        except User.DoesNotExist:
            try:
                user = User.objects.get(username=username)
                # print("authenticate:", username)
            except User.DoesNotExist:
                return None

            if user.check_password(password):
                # print("authenticate:", "Check for password ")
                return user
            # print("authenticate:", "NONE")
            return None

    def get_user(self, user_id):
        try:
            return User.objects.get(id=user_id)
        except User.DoesNotExist:
            return None
