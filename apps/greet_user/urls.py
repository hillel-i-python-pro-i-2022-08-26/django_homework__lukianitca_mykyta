from django.urls import path
from . import views

urlpatterns = [
    path("", views.greet_user),
    path("<str:username>", views.greet_user),
]
