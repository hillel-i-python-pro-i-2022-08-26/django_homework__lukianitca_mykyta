# Generated by Django 4.1.3 on 2022-11-10 17:03

from django.db import migrations, models

import apps.services.image_paths


class Migration(migrations.Migration):

    dependencies = [
        ("superuser_hw", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="avatar",
            field=models.ImageField(
                blank=True, max_length=255, null=True, upload_to=apps.services.image_paths.get_avatar_path_user
            ),
        ),
    ]
