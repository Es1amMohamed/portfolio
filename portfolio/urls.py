from django.urls import path
from . import views
from .views import *

app_name = "portfolio"

urlpatterns = [
    path("", views.main, name="main"),
    path("contact/", views.contact, name="contact"),
    path("projects/", views.Projects_view.as_view(), name="projects"),
    path("projects/<str:slug>", views.single_project, name="single_project"),
    path("blogs/", views.Blogs_view.as_view(), name="blogs"),
    path("blogs/<str:slug>", views.single_blog, name="single_blog"),
    path("download/", views.download_file, name="download"),
]
