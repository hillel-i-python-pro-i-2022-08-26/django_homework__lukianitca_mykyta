# Generated by Django 4.1.1 on 2022-10-12 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("contacts", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="contacts",
            name="birth_date",
            field=models.DateField(),
        ),
    ]
