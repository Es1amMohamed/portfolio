# Generated by Django 4.2.5 on 2023-10-18 18:31

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("portfolio", "0011_colleagues_is_approve"),
    ]

    operations = [
        migrations.CreateModel(
            name="AboutMe",
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
                ("first_name", models.CharField(blank=True, max_length=60)),
                ("last_name", models.CharField(blank=True, max_length=60)),
                ("years_of_experience", models.IntegerField(default=0)),
                ("bio", models.TextField(max_length=1000)),
                ("personal_picture", models.ImageField(upload_to="personal_picture")),
                ("cv", models.FileField(upload_to="cv")),
                ("phone_number", models.CharField(max_length=20)),
                ("email", models.EmailField(max_length=200)),
                ("facebook_link", models.URLField()),
                ("github_link", models.URLField()),
                ("linkedin_link", models.URLField()),
                ("address", models.CharField(max_length=200)),
            ],
        ),
        migrations.RenameField(
            model_name="portfolio",
            old_name="bio",
            new_name="experience_bio",
        ),
        migrations.RenameField(
            model_name="portfolio",
            old_name="bio2",
            new_name="skills_bio",
        ),
        migrations.RemoveField(
            model_name="portfolio",
            name="cv",
        ),
        migrations.RemoveField(
            model_name="portfolio",
            name="first_name",
        ),
        migrations.RemoveField(
            model_name="portfolio",
            name="last_name",
        ),
        migrations.RemoveField(
            model_name="portfolio",
            name="personal_picture",
        ),
        migrations.RemoveField(
            model_name="portfolio",
            name="years_of_experience",
        ),
        migrations.AddField(
            model_name="portfolio",
            name="icon",
            field=models.ImageField(blank=True, upload_to="icons"),
        ),
    ]
