from django.shortcuts import render
from webargs import fields
from webargs.djangoparser import use_args

from apps.greet_user.services import generate_fake_name


@use_args({"username": fields.Str(missing=generate_fake_name())}, location="query")
def greet_user(request, args: dict):
    username = args["username"]
    return render(request, "greet_user/index.html", {"username": username})
