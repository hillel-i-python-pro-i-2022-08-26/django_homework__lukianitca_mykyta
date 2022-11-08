from django.urls import path

from apps.contacts import views

app_name = "contacts"

urlpatterns = [
    path("show-contacts/", views.ListContacts.as_view(), name="show_contacts"),
    path("add-contact/", views.CreateContact.as_view(), name="add_contact"),
    path("detail-contact/<int:pk>/", views.DetailContact.as_view(), name="detail_contact"),
    path("update-contact/<int:pk>/", views.UpdateContact.as_view(), name="update_contact"),
    path("delete-contact/<int:pk>/", views.DeleteContact.as_view(), name="delete_contact"),
]
