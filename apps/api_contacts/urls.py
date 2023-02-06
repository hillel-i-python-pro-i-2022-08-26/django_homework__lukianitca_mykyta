from django.urls import path, include
from rest_framework import routers

from apps.api_contacts import views

contacts_router = routers.DefaultRouter()
contacts_router.register(r"contacts", views.ContactsViewSet, basename="contact")

app_name = ""

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path("", include(contacts_router.urls)),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
]
