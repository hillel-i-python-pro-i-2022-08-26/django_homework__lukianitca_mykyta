from django.urls import path
from apps.contacts import views

urlpatterns = [
    path("show_contacts", views.ShowContacts.as_view(), name="show_contacts"),
]
