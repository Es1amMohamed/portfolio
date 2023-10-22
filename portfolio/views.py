from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import *
from django.views import View
from django.views.generic import ListView
from django.core.mail import send_mail, BadHeaderError
from django.contrib import messages

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
        messages.success(
            request, "Thank you for your message. We will get back to you soon."
        )
        return redirect("/")
    return render(request, "portfolio/contact.html")


def colleagues(request):
    return render(request, "portfolio/colleagues.html")


def skillsandtools(request):
    pass

# <script src="https://platform.linkedin.com/badges/js/profile.js" async defer type="text/javascript"></script>
# <div class="badge-base LI-profile-badge" data-locale="en_US" data-size="medium" data-theme="dark" data-type="VERTICAL" data-vanity="eslam-mohamed-aa3b87239" data-version="v1"><a class="badge-base__link LI-simple-link" href="https://eg.linkedin.com/in/eslam-mohamed-aa3b87239?trk=profile-badge">Eslam Mohamed</a></div>
              