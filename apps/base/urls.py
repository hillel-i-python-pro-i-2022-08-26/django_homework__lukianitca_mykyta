from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("greetings/", views.greetings, name="greetings"),
    path("greetings/<str:username>", views.greetings, name="greetings"),
]
