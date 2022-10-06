from django.urls import path
from . import views

app_name = "base"

urlpatterns = [
    path("", views.index, name="index"),
    path("greetings/", views.greetings, name="greetings"),
    path("greetings/<str:username>", views.greetings),
]
