# Generated by Django 4.2.5 on 2023-10-20 14:48

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("portfolio", "0012_aboutme_rename_bio_portfolio_experience_bio_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Contact",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("email", models.EmailField(max_length=200)),
                ("phone", models.CharField(blank=True, max_length=25, null=True)),
                ("message", models.TextField(max_length=1000)),
            ],
        ),
    ]