from django.shortcuts import render
from django.utils import timezone
from django.views.generic import ListView

from apps.contacts.models import Contacts


class ShowContacts(ListView):
    model = Contacts
    template_name = "contacts/show_contacts.html"
    context_object_name = "contacts"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context
