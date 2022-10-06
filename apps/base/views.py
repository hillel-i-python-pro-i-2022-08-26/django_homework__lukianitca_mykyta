from django.shortcuts import render

from apps.base.services import FakeEngine, UsersDataGenerator


def index(request):
    return render(request, "base/index.html", {"title": "Main page"})


def greetings(request, username: str | None = None):
    if not username:
        username = FakeEngine().generate_fake_name()
    context = {
        "username": username,
        "title": "Greetings",
        "current_offers": [f"Offer {i}" for i in range(1, 6)],
    }
    return render(request, "base/greet_user.html", context)


def users_info(request, amount_users: int | None = None):
    users_list = UsersDataGenerator(amount_users).unique_users
    return render(request, "")
