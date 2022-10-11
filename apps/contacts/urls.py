from django.urls import path
from apps.contacts import views

app_name = "contacts"

urlpatterns = [
    path("show-contacts/", views.show_contacts, name="show_contacts"),
]
