import datetime

from django import forms
from django.utils import timezone

from apps.contacts import models


class ContactForm(forms.ModelForm):
    class Meta:
        model = models.Contact
        fields = ("contact_name", "phone_number", "birth_date", "contact_photo")
        widgets = {
            "birth_date": forms.DateInput(
                attrs={
                    "type": "date",
                    "min": datetime.date(day=1, month=1, year=1910),
                    "max": datetime.date(day=1, month=1, year=timezone.now().year - 11),
                }
            ),
        }
