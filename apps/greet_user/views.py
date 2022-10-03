from django.shortcuts import render

from apps.base.services import generate_fake_name


def greetings(request, username: str | None = None):
    if not username:
        username = generate_fake_name()
    return render(request, "greet_user/index.html", {"username": username, "title": "Greetings"})
