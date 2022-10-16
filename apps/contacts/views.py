from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect

from apps.contacts.forms import ContactForm
from apps.contacts.models import Contact


def show_contacts(request: HttpRequest) -> HttpResponse:
    contacts_list = Contact.objects.all()
    return render(request, "contacts/show_contacts.html", {"title": "Contacts List", "contacts": contacts_list})


def detail_contact(request: HttpRequest, contact_id: int) -> HttpResponse:
    contact_obj = Contact.objects.get(pk=contact_id)
    return render(request, "contacts/detail_contact.html", {"title": "Detail Contact", "contact": contact_obj})


def add_contact(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            new_contact = form.save()
            return redirect(new_contact)
        return render(request, "contacts/add_contact.html", {"title": "Add Contact", "form": form})
    else:
        form = ContactForm()
    return render(request, "contacts/add_contact.html", {"title": "Add Contact", "form": form})


def update_contact(request: HttpRequest, contact_id: int) -> HttpResponse:
    contact_obj = Contact.objects.get(pk=contact_id)
    if request.method == "POST":
        form = ContactForm(request.POST, instance=contact_obj)
        if form.is_valid():
            updated_contact = form.save()
            return redirect(updated_contact)
        return render(request, "contacts/update_contact.html", {"title": "Update Contact", "form": form})
    else:
        form = ContactForm(instance=contact_obj)
    return render(request, "contacts/update_contact.html", {"title": "Update Contact", "form": form})


def delete_contact(request: HttpRequest, contact_id: int) -> HttpResponse:
    Contact.objects.get(pk=contact_id).delete()
    return redirect("contacts:show_contacts")
