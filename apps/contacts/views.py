from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect

from apps.contacts.forms import AddContactForm
from apps.contacts.models import Contacts


def show_contacts(request: HttpRequest) -> HttpResponse:
    contacts_list = Contacts.objects.all()
    return render(request, "contacts/show_contacts.html", {"title": "Contacts List", "contacts": contacts_list})


def add_contact(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = AddContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("contacts:show_contacts")
        return render(request, "contacts/add_contact.html", {"title": "Add Contact", "form": form})
    else:
        form = AddContactForm()
    return render(request, "contacts/add_contact.html", {"title": "Add Contact", "form": form})
