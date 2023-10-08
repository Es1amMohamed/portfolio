# Generated by Django 4.2.5 on 2023-10-08 19:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("portfolio", "0005_remove_portfolio_name_portfolio_first_name_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Blogs",
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
                (
                    "image",
                    models.ImageField(blank=True, null=True, upload_to="blogs_images"),
                ),
                ("description", models.TextField(max_length=1000)),
                ("slug", models.SlugField(blank=True, null=True)),
                (
                    "author",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="portfolio.portfolio",
                    ),
                ),
            ],
        ),
    ]
