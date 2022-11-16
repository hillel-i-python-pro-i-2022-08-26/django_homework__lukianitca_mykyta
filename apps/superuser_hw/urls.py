from django.urls import path

from apps.superuser_hw import views

app_name = "auth_user_app"

urlpatterns = [
    path("sign-up/", views.RegisterUserView.as_view(), name="sign_up"),
    path("login/", views.LoginUserView.as_view(), name="login"),
    path("logout/", views.LogoutUserView.as_view(), name="logout"),
]
