# Generated by Django 4.1.3 on 2023-02-06 17:12

import uuid

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models

import apps.services.image_paths


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("contacts", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Contact",
            fields=[
                ("id", models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ("contact_name", models.CharField(max_length=120)),
                ("phone_number", models.CharField(max_length=40)),
                (
                    "contact_photo",
                    models.ImageField(
                        blank=True,
                        max_length=255,
                        null=True,
                        upload_to=apps.services.image_paths.get_contact_photo_path,
                    ),
                ),
                ("birth_date", models.DateField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="contacts",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "ordering": ["contact_name"],
            },
        ),
        migrations.DeleteModel(
            name="Contacts",
        ),
    ]
