from django.db import models
from django.core.validators import FileExtensionValidator


class Portfolio(models.Model):
    name = models.CharField(max_length=50)
    main_image = models.ImageField(upload_to="main image")
    years_of_experience = models.IntegerField(default=0)
    projects = ""
    colleagues = ""
    bio = models.TextField(max_length=1000)
    bio2 = models.TextField(max_length=1000)
    cv = models.FileField(upload_to="cv")
    personal_picture = models.ImageField(upload_to="personal_picture")

    def __str__(self):
        return self.name


class Skills(models.Model):
    name = models.CharField(max_length=50)
    icon = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Tools(models.Model):
    name = models.CharField(max_length=50)
    icon = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Projects(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to="projects images")
    start_date = models.DateTimeField()
    description = models.TextField(max_length=1000)
    category = ""
    video = models.FileField(
        upload_to="videos_uploaded",
        null=True,
        validators=[
            FileExtensionValidator(
                allowed_extensions=["MOV", "avi", "mp4", "webm", "mkv"]
            )
        ],
    )
    repo_link = models.URLField(max_length=200)


class Colleagues(models.Model):
    name = models.CharField(max_length=100)
    job_title = models.CharField(max_length=100)
    comment = models.TextField(max_length=500)
    image = models.ImageField(upload_to="colleagues_images")
    workplace = models.CharField(max_length=50)


class Category(models.Model):
    pass
