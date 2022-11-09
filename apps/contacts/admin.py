from django.contrib import admin
from django.contrib.admin import ModelAdmin

from apps.contacts.forms import ContactForm
from apps.contacts.models import Contact


class ContactAdmin(ModelAdmin):
    form = ContactForm


admin.site.register(Contact, ContactAdmin)
