from django.urls import path
from . import views

app_name = "greet_user"

urlpatterns = [
    path("", views.greetings, name="greetings"),
    path("<str:username>", views.greetings, name="greetings"),
]
