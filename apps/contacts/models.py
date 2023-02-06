from django.db import models
from django.urls import reverse_lazy

from apps.services.image_paths import get_contact_photo_path
from apps.superuser_hw.models import User


class Contact(models.Model):
    contact_name = models.CharField(max_length=120)
    phone_number = models.CharField(max_length=40)
    contact_photo = models.ImageField(
        max_length=255,
        null=True,
        blank=True,
        upload_to=get_contact_photo_path,
    )
    birth_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, related_name="contacts", on_delete=models.CASCADE)

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
