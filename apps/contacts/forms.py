import datetime

from django import forms
from django.core.exceptions import ValidationError
from django.utils import timezone

from apps.contacts import models


class AddContactForm(forms.ModelForm):
    def clean_birth_date(self):
        date = self.cleaned_data.get("birth_date")
        minimal_date = {"day": 1, "month": 1, "year": 1910}
        maximal_date = {"day": 1, "month": 1, "year": timezone.now().year - 11}
        if not datetime.date(**maximal_date) > date > datetime.date(**minimal_date):
            raise ValidationError("This date is invalid")
        return date

    class Meta:
        model = models.Contacts
        fields = ("contact_name", "phone_number", "birth_date")
        widgets = {
            'birth_date': forms.DateInput(attrs={"type": "date"})
        }
