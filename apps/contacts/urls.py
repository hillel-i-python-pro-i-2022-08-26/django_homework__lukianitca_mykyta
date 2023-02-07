from django.urls import path

from apps.contacts import views

app_name = "contacts"

urlpatterns = [
    path("show-contacts/", views.ListContacts.as_view(), name="show_contacts"),
    path("add-contact/", views.CreateContact.as_view(), name="add_contact"),
    path("detail-contact/<uuid:pk>/", views.DetailContact.as_view(), name="detail_contact"),
    path("update-contact/<uuid:pk>/", views.UpdateContact.as_view(), name="update_contact"),
    path("delete-contact/<uuid:pk>/", views.DeleteContact.as_view(), name="delete_contact"),
]
