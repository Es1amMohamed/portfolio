# Generated by Django 4.2.5 on 2023-09-29 17:06

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Category",
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
            ],
        ),
        migrations.CreateModel(
            name="Colleagues",
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
                ("job_title", models.CharField(max_length=100)),
                ("comment", models.TextField(max_length=500)),
                ("image", models.ImageField(upload_to="colleagues_images")),
                ("workplace", models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name="Portfolio",
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
                ("name", models.CharField(max_length=50)),
                ("main_image", models.ImageField(upload_to="main image")),
                ("years_of_experience", models.IntegerField(default=0)),
                ("bio", models.TextField(max_length=1000)),
                ("bio2", models.TextField(max_length=1000)),
                ("cv", models.FileField(upload_to="cv")),
                ("personal_picture", models.ImageField(upload_to="personal_picture")),
            ],
        ),
        migrations.CreateModel(
            name="Projects",
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
                ("title", models.CharField(max_length=100)),
                ("image", models.ImageField(upload_to="projects images")),
                ("start_date", models.DateTimeField()),
                ("description", models.TextField(max_length=1000)),
                (
                    "video",
                    models.FileField(
                        null=True,
                        upload_to="videos_uploaded",
                        validators=[
                            django.core.validators.FileExtensionValidator(
                                allowed_extensions=["MOV", "avi", "mp4", "webm", "mkv"]
                            )
                        ],
                    ),
                ),
                ("repo_link", models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name="Skills",
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
                ("name", models.CharField(max_length=50)),
                ("icon", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="Tools",
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
                ("name", models.CharField(max_length=50)),
                ("icon", models.CharField(max_length=100)),
            ],
        ),
    ]
