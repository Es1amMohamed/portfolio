# Generated by Django 4.2.5 on 2023-10-23 17:45

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("portfolio", "0014_contact_created_at"),
    ]

    operations = [
        migrations.AlterField(
            model_name="colleagues",
            name="image",
            field=models.ImageField(
                default="default.jpg", upload_to="colleagues_images"
            ),
        ),
    ]
