from django.db import models
from django.core.validators import FileExtensionValidator
from django.utils.text import slugify


class Portfolio(models.Model):
    first_name = models.CharField(max_length=60, blank=True)
    last_name = models.CharField(max_length=60, blank=True)
    main_image = models.ImageField(upload_to="main image")
    years_of_experience = models.IntegerField(default=0)
    bio = models.TextField(max_length=1000)
    bio2 = models.TextField(max_length=1000)
    cv = models.FileField(upload_to="cv")
    personal_picture = models.ImageField(upload_to="personal_picture")

    def __str__(self):
        return self.first_name


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
    end_date = models.DateTimeField(null=True, blank=True)
    description = models.TextField(max_length=1000)
    category = models.ForeignKey(
        "Category", on_delete=models.CASCADE, blank=True, null=True
    )
    skills_used = models.ManyToManyField(Skills, blank=True)
    Tools_used = models.ManyToManyField(Tools, blank=True)
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
    slug = models.SlugField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)

        super(Projects, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


class Colleagues(models.Model):
    name = models.CharField(max_length=100)
    job_title = models.CharField(max_length=100)
    comment = models.TextField(max_length=500)
    image = models.ImageField(upload_to="colleagues_images")
    workplace = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100, default="Django")

    def __str__(self):
        return self.name


class Blogs(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Portfolio, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="blogs_images", null=True, blank=True)
    description = models.TextField(max_length=1000)
    slug = models.SlugField(null=True, blank=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)

        super(Blogs, self).save(*args, **kwargs)


class CoursesAndCertificates(models.Model):
    title = models.CharField(max_length=100)
    course_link = models.URLField(max_length=200)
    certificate_link = models.URLField(max_length=200, null=True, blank=True)
    description = models.TextField(max_length=1000)
    slug = models.SlugField(null=True, blank=True)
    
    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)

        super(CoursesAndCertificates, self).save(*args, **kwargs)