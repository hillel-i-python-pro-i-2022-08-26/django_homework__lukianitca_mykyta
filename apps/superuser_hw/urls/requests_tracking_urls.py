from django.urls import path

from apps.superuser_hw import views

app_name = "request_tracking"

urlpatterns = [
    path("show-all/", views.AllRequestsView.as_view(), name="all_requests"),
]
