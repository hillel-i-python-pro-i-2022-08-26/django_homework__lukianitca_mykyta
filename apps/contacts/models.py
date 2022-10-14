from django.db import models


class Contact(models.Model):
    contact_name = models.CharField(max_length=120)
    phone_number = models.CharField(max_length=40)
    birth_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created_at']
