from django.urls import path

from apps.superuser_hw import views

app_name = "request_tracking"

urlpatterns = [
    path("show-all/", views.AllRequestsView.as_view(), name="all_requests"),
    path("show-session/", views.SessionRequestsView.as_view(), name="session_requests"),
    path("show-users/", views.UsersRequestsView.as_view(), name="users_requests"),
]
