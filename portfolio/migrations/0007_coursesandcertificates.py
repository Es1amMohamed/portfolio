# Generated by Django 4.2.5 on 2023-10-11 19:49

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("portfolio", "0006_blogs"),
    ]

    operations = [
        migrations.CreateModel(
            name="CoursesAndCertificates",
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
                ("course_link", models.URLField()),
                ("certificate_link", models.URLField()),
                ("description", models.TextField(max_length=1000)),
                ("slug", models.SlugField(blank=True, null=True)),
            ],
        ),
    ]