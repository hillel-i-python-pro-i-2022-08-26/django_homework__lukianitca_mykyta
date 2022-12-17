from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic import CreateView

from apps.superuser_hw.forms import UserCreationFormCustom


class RegisterUserView(CreateView):
    form_class = UserCreationFormCustom
    template_name = "auth_templates/auth_form.html"
    success_url = reverse_lazy("auth_user_app:login")


class LoginUserView(LoginView):
    form_class = AuthenticationForm
    template_name = "auth_templates/auth_form.html"


class LogoutUserView(LogoutView):
    next_page = reverse_lazy("base:index")
