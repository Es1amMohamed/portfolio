from django.shortcuts import render
from .models import *
from django.views import View
from django.views.generic import ListView

# Create your views here.


def main(request):
    return render(request, "portfolio/portfolio.html")


class Projects(ListView):
    model = Projects
    template_name = "portfolio/projects.html"


class Blogs(ListView):
    model = Blogs
    template_name = "portfolio/blogs.html"


def single_project(request):
    pass


def single_blog(request):
    pass


def contact(request):
    return render(request, "portfolio/contact.html")


def colleagues(request):
    return render(request, "portfolio/colleagues.html")


def skillsandtools(request):
    pass
