# Generated by Django 4.2.5 on 2023-11-04 20:12

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("portfolio", "0032_alter_coursesandcertificates_title"),
    ]

    operations = [
        migrations.AddField(
            model_name="coursesandcertificates",
            name="end_date",
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name="coursesandcertificates",
            name="start_date",
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
