from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic

from apps.contacts.forms import ContactForm
from apps.contacts.models import Contact
from apps.contacts.services import update_request_obj


class ListContacts(LoginRequiredMixin, generic.ListView):
    template_name = "contacts/show_contacts.html"
    context_object_name = "contacts"
    model = Contact
    login_url = reverse_lazy("auth_user_app:login")

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(
            {
                "title": "Contacts List",
                "contacts_visited": self.request.session.get("visited", 0),
                "last_visit": self.request.session.get("last_visit", "Contacts haven't been visited yet"),
            }
        )
        return context


class DetailContact(generic.DetailView):
    model = Contact
    template_name = "contacts/detail_contact.html"

    def get(self, request, *args, **kwargs):
        request = update_request_obj(request)
        return super().get(request, *args, **kwargs)


class CreateContact(generic.CreateView):
    form_class = ContactForm
    template_name = "contacts/add_contact.html"


class UpdateContact(generic.UpdateView):
    form_class = ContactForm
    model = Contact
    template_name = "contacts/update_contact.html"


class DeleteContact(generic.DeleteView):
    model = Contact
    success_url = reverse_lazy("contacts:show_contacts")
