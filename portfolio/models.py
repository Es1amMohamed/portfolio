from django.utils import timezone
from django.db import models
from django.core.validators import FileExtensionValidator
from django.utils.text import slugify


class Portfolio(models.Model):
    title = models.CharField(max_length=60, blank=True)
    icon = models.ImageField(blank=True, upload_to="icons")
    main_image = models.ImageField(upload_to="main image")
    skills_bio = models.TextField(max_length=1000)
    experience_bio = models.TextField(max_length=1000)

    def __str__(self):
        return self.title


class AboutMe(models.Model):
    first_name = models.CharField(max_length=60, blank=True)
    last_name = models.CharField(max_length=60, blank=True)
    years_of_experience = models.IntegerField(default=0)
    bio = models.TextField(max_length=1000)
    bio_2 = models.TextField(max_length=1000, null=True, blank=True)
    personal_picture = models.ImageField(upload_to="personal_picture")
    cv = models.FileField(upload_to="cv")
    phone_number = models.CharField(max_length=20)
    phone_number_2 = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField(max_length=200)
    email_2 = models.EmailField(max_length=200, null=True, blank=True)
    facebook_link = models.URLField(max_length=200)
    github_link = models.URLField(max_length=200)
    linkedin_link = models.URLField(max_length=200)
    address = models.CharField(max_length=200)

    def __str__(self):
        return self.first_name


class Skills(models.Model):
    name = models.CharField(max_length=50)
    icon = models.ImageField(upload_to="skills_icon")

    def __str__(self):
        return self.name


class Tools(models.Model):
    name = models.CharField(max_length=50)
    icon = models.ImageField(upload_to="tools_icon")

    def __str__(self):
        return self.name


class Projects(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to="projects_images", null=True, blank=True)
    video_poster = models.ImageField(upload_to="video_posters", null=True, blank=True)
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
    image = models.ImageField(upload_to="colleagues_images", default="default.png")
    workplace = models.CharField(max_length=50)
    created_at = models.DateTimeField(default=timezone.now)
    is_approve = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100, default="Django")

    def __str__(self):
        return self.name


class Blogs(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to="blogs_images", null=True, blank=True)
    caption = models.CharField(max_length=1000, null=True, blank=True)
    description = models.TextField(max_length=1000)
    created_at = models.DateTimeField(default=timezone.now)
    slug = models.SlugField(null=True, blank=True)
    objects = models.Manager()

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


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=200)
    phone = models.CharField(max_length=25, null=True, blank=True)
    message = models.TextField(max_length=1000)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name
