# Generated by Django 4.2.5 on 2023-11-07 19:05

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):
    dependencies = [
        ("portfolio", "0034_rename_coursesandcertificates_courses"),
    ]

    operations = [
        migrations.AlterField(
            model_name="blogs",
            name="caption",
            field=models.CharField(
                blank=True, max_length=1000, null=True, verbose_name="caption"
            ),
        ),
        migrations.AlterField(
            model_name="blogs",
            name="created_at",
            field=models.DateTimeField(
                default=django.utils.timezone.now, verbose_name="created_at"
            ),
        ),
        migrations.AlterField(
            model_name="blogs",
            name="description",
            field=models.TextField(max_length=1000, verbose_name="description"),
        ),
        migrations.AlterField(
            model_name="blogs",
            name="image",
            field=models.ImageField(
                blank=True, null=True, upload_to="blogs_images", verbose_name="image"
            ),
        ),
        migrations.AlterField(
            model_name="blogs",
            name="slug",
            field=models.SlugField(blank=True, null=True, verbose_name="url"),
        ),
        migrations.AlterField(
            model_name="blogs",
            name="title",
            field=models.CharField(max_length=100, verbose_name="title"),
        ),
    ]
