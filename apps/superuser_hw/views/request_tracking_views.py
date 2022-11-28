from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from apps.superuser_hw.models import Request
from apps.superuser_hw.services import normalize_session_key
from apps.superuser_hw.views.base_views import BaseRequestsView


class AllRequestsView(BaseRequestsView):
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "All Requests"
        return context


class SessionRequestsView(BaseRequestsView):
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Session Requests"
        return context

    def get_queryset(self):
        session_key = normalize_session_key(self.request.session)
        return Request.objects.filter(session_key=session_key)


class UsersRequestsView(LoginRequiredMixin, BaseRequestsView):
    login_url = reverse_lazy("auth_user_app:login")

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "User's Requests"
        return context

    def get_queryset(self):
        return self.request.user.requests_info.all()
