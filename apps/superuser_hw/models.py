from django.contrib.auth.models import AbstractUser
from django.db import models

from apps.services.image_paths import get_avatar_path_user


class User(AbstractUser):
    avatar = models.ImageField(
        max_length=255,
        null=True,
        blank=True,
        upload_to=get_avatar_path_user,
    )
