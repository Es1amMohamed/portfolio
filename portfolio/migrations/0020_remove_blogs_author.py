# Generated by Django 4.2.5 on 2023-10-30 21:15

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("portfolio", "0019_projects_image"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="blogs",
            name="author",
        ),
    ]
