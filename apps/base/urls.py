from django.urls import path

from . import views

app_name = "base"

greet_user_homework = [
    path("", views.IndexPage.as_view(), name="index"),
    path("greetings/", views.GreetingsPage.as_view(), name="greetings"),
    path("greetings/<str:username>", views.GreetingsPage.as_view()),
]


generate_accounts_homework = [
    path("unique-users/", views.UsersInfoView.as_view(), name="unique_users"),
    path("unique-users/<int:amount_users>", views.UsersInfoView.as_view()),
]

urlpatterns = greet_user_homework + generate_accounts_homework
