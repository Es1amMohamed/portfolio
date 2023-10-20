from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import *
from django.views import View
from django.views.generic import ListView
from django.core.mail import send_mail, BadHeaderError

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
    if request.method == "POST":
        sender_name = request.POST["name"]
        sender_email = request.POST["email2"]
        sender_phone = request.POST["phone"]
        message = request.POST["message2"]
        print(message)
        print(sender_email)
        contact = Contact.objects.create(
            name=sender_name, email=sender_email, phone=sender_phone, message=message
        )
        contact.save()
        return redirect("/")
    return render(request, "portfolio/contact.html")


def colleagues(request):
    return render(request, "portfolio/colleagues.html")


def skillsandtools(request):
    pass
