# Generated by Django 4.2.5 on 2023-12-08 13:51

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("portfolio", "0045_skills_link"),
    ]

    operations = [
        migrations.AlterField(
            model_name="blogs",
            name="description",
            field=models.TextField(max_length=5000, verbose_name="description"),
        ),
    ]