from django.shortcuts import render

from apps.contacts.models import Contacts


def show_contacts(request):
    contacts_list = Contacts.objects.all()
    return render(request, "contacts/show_contacts.html", {"title": "Contacts List", "contacts": contacts_list})
