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


class Request(models.Model):
    session_key = models.CharField(max_length=100)
    path = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, related_name="requests_info", null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    visits_count = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.session_key} - {self.path} - {self.user or 'Anonymous'}"

    class Meta:
        constraints = (
            models.UniqueConstraint(
                fields=("session_key", "path", "user"),
                name="Path with these parameters already exists",
            ),
        )
