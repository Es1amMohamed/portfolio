from django.urls import path
from . import views
from .views import *

app_name = "portfolio"

urlpatterns = [
    path("", views.main, name="main"),
    path("contact/", views.contact, name="contact"),
    path("projects/", views.Projects.as_view(), name="projects"),
    path("blogs/", views.Blogs.as_view(), name="blogs"),
]
