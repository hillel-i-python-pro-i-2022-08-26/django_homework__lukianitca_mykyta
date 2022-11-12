from django.contrib.auth.forms import UserCreationForm

from .models import User


class UserCreationFormCustom(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "email", "avatar", "password1", "password2")
