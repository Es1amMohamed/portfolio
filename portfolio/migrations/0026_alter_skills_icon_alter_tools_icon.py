# Generated by Django 4.2.5 on 2023-11-03 18:30

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("portfolio", "0025_aboutme_email_2_aboutme_phone_number_2"),
    ]

    operations = [
        migrations.AlterField(
            model_name="skills",
            name="icon",
            field=models.ImageField(upload_to="skills_icon"),
        ),
        migrations.AlterField(
            model_name="tools",
            name="icon",
            field=models.ImageField(upload_to="tools_icon"),
        ),
    ]
