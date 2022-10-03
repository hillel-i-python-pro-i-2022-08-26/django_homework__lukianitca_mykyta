from django.urls import path
from . import views

homework_greetings = [
    path("", views.index, name="index"),
    path("greetings/", views.greetings, name="greetings"),
    path("greetings/<str:username>", views.greetings, name="greetings"),
]


homework_generate_users = []


urlpatterns = homework_greetings + homework_generate_users
