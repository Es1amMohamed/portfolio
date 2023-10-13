from django.shortcuts import render
from .models import *
from django.views import View

# Create your views here.


def main(request):
    return render(request, "portfolio/portfolio.html")


class AboutMe(View):
    pass


class Projects(View):
    pass


class Blogs(View):
    pass


def single_project(request):
    pass


def single_blog(request):
    pass


def contact(request):
    pass


def colleagues(request):
    pass
