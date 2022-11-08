from django.db import models
from django.urls import reverse_lazy


class Contact(models.Model):
    contact_name = models.CharField(max_length=120)
    phone_number = models.CharField(max_length=40)
    birth_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse_lazy("contacts:detail_contact", kwargs={"pk": self.pk})

    def get_update_url(self):
        return reverse_lazy("contacts:update_contact", kwargs={"pk": self.pk})

    def get_delete_url(self):
        return reverse_lazy("contacts:delete_contact", kwargs={"pk": self.pk})

    def __str__(self):
        return self.contact_name

    class Meta:
        ordering = ["contact_name"]
