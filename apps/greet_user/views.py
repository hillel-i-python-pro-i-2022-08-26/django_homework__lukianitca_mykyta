from django.shortcuts import render
from webargs import fields

from apps.greet_user.services import generate_fake_name


def greet_user(request, username: str | None = None):
    if not username:
        username = generate_fake_name()
    return render(request, "greet_user/index.html", {"username": username})
