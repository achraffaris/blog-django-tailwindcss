# Generated by Django 4.2.4 on 2023-08-22 16:44

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="blog",
            name="image",
            field=cloudinary.models.CloudinaryField(
                max_length=255, verbose_name="articles"
            ),
        ),
    ]
