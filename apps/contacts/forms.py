import datetime

from django import forms
from django.core.exceptions import ValidationError
from django.utils import timezone

from apps.contacts import models


class ContactForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.minimal_date = datetime.date(day=1, month=1, year=1910)
        self.maximal_date = datetime.date(day=1, month=1, year=timezone.now().year - 11)

    def clean_birth_date(self):
        date = self.cleaned_data.get("birth_date")
        if not self.maximal_date > date > self.minimal_date:
            raise ValidationError("This date is invalid")
        return date

    class Meta:
        model = models.Contact
        fields = ("contact_name", "phone_number", "birth_date")
        widgets = {
            "birth_date": forms.DateInput(
                attrs={
                    "type": "date",
                    "min": datetime.date(day=1, month=1, year=1910),
                    "max": datetime.date(day=1, month=1, year=timezone.now().year - 11),
                }
            ),
        }
