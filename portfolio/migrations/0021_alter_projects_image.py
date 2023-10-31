# Generated by Django 4.2.5 on 2023-10-31 19:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("portfolio", "0020_remove_blogs_author"),
    ]

    operations = [
        migrations.AlterField(
            model_name="projects",
            name="image",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="project_image",
                to="portfolio.project_images",
            ),
        ),
    ]