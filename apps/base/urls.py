from django.urls import path

from . import views

app_name = "base"

greet_user_homework = [
    path("", views.index, name="index"),
    path("greetings/", views.greetings, name="greetings"),
    path("greetings/<str:username>", views.greetings),
]


generate_accounts_homework = [
    path("unique-users/", views.users_info, name="unique_users"),
    path("unique-users/<int:amount_users>", views.users_info),
]

urlpatterns = greet_user_homework + generate_accounts_homework
