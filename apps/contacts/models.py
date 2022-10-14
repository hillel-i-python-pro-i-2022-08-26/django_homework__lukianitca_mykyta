from django.db import models
from django.urls import reverse


class Contact(models.Model):
    contact_name = models.CharField(max_length=120)
    phone_number = models.CharField(max_length=40)
    birth_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse("contacts:detail_contact", kwargs={"user_id": self.pk})

    class Meta:
        ordering = ['created_at']
