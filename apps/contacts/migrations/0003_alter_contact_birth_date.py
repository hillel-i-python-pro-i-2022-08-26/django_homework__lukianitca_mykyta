# Generated by Django 4.1.3 on 2023-02-07 13:44

from django.db import migrations, models

import apps.services.validators


class Migration(migrations.Migration):

    dependencies = [
        ("contacts", "0002_contact_delete_contacts"),
    ]

    operations = [
        migrations.AlterField(
            model_name="contact",
            name="birth_date",
            field=models.DateField(validators=[apps.services.validators.birth_date_validator]),
        ),
    ]
