# Generated by Django 4.2.5 on 2023-10-06 15:55

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        (
            "portfolio",
            "0002_category_name_projects_category_projects_end_date_and_more",
        ),
    ]

    operations = [
        migrations.AddField(
            model_name="projects",
            name="Tools_used",
            field=models.ManyToManyField(blank=True, to="portfolio.tools"),
        ),
        migrations.AddField(
            model_name="projects",
            name="skills_used",
            field=models.ManyToManyField(blank=True, to="portfolio.skills"),
        ),
        migrations.AddField(
            model_name="skills",
            name="project",
            field=models.ManyToManyField(blank=True, to="portfolio.projects"),
        ),
        migrations.AddField(
            model_name="tools",
            name="project",
            field=models.ManyToManyField(blank=True, to="portfolio.projects"),
        ),
    ]
