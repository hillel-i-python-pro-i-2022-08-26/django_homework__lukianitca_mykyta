from django.urls import path

from apps.contacts import views

app_name = "contacts"

urlpatterns = [
    path("show-contacts/", views.show_contacts, name="show_contacts"),
    path("detail-contact/user_id", views.detail_contact, name="detail_contact"),
    path("add-contact/", views.add_contact, name='add_contact'),
]
