from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

from apps.contacts.forms import AddContactForm
from apps.contacts.models import Contact


def show_contacts(request: HttpRequest) -> HttpResponse:
    contacts_list = Contact.objects.all()
    return render(request, "contacts/show_contacts.html", {"title": "Contacts List", "contacts": contacts_list})


def detail_contact(request, contact_id):
    contact_obj = Contact.objects.get(pk=contact_id)
    return render(request, "contacts/detail_contact.html", {"title": "Detail Contact", "contact": contact_obj})


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


def update_contact(request, contact_id):
    contact_obj = Contact.objects.get(pk=contact_id)
    if request.method == "POST":
        form = AddContactForm(request.POST, instance=contact_obj)
        if form.is_valid():
            updated_contact = form.save()
            return redirect(updated_contact)
        return render(request, "contacts/update_contact.html", {"title": "Update Contact", "form": form})
    else:
        form = AddContactForm(instance=contact_obj)
    return render(request, "contacts/update_contact.html", {"title": "Update Contact", "form": form})


def delete_contact(request, contact_id):
    obj = get_object_or_404(Contact, pk=contact_id)
    obj.delete()
    return redirect("contacts:show_contacts")
