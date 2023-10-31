from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import *
from django.views import View
from django.views.generic import ListView
from django.core.mail import send_mail, BadHeaderError
from django.contrib import messages
from django.shortcuts import get_object_or_404

# Create your views here.


def main(request):
    all_colleagues = Colleagues.objects.filter(is_approve=True)
    if request.method == "POST":
        if request.FILES.get("image") == None:
            colleagues_name = request.POST["name"]
            job_title = request.POST["jobtitle"]
            workplace = request.POST["workplace"]
            comment = request.POST["comment2"]

            colleagues = Colleagues.objects.create(
                name=colleagues_name,
                job_title=job_title,
                workplace=workplace,
                comment=comment,
            )
            colleagues.save()
            messages.success(
                request, "Thank you for your comment. I will approve to it soon."
            )
            return redirect("/")
        if request.FILES["image"] != None:
            colleagues_name = request.POST["name"]
            job_title = request.POST["jobtitle"]
            workplace = request.POST["workplace"]
            comment = request.POST["comment2"]
            image = request.FILES["image"]

            colleagues = Colleagues.objects.create(
                name=colleagues_name,
                job_title=job_title,
                workplace=workplace,
                comment=comment,
                image=image,
            )
            colleagues.save()
            messages.success(
                request, "Thank you for your comment. I will approve to it soon."
            )
            return redirect("/")

    if len(all_colleagues) == 0:
        colleagues = "Be the first to comment."
        return render(request, "portfolio/portfolio.html", {"colleague": colleagues})
    return render(request, "portfolio/portfolio.html", {"colleagues": all_colleagues})


class Projects_view(ListView):
    model = Projects
    context_object_name = "projects"
    template_name = "portfolio/projects.html"


class Blogs_view(ListView):
    model = Blogs
    context_object_name = "blogs"
    template_name = "portfolio/blogs.html"


def single_project(request, slug):
    project = Projects.objects.get(slug=slug)
    return render(request, "portfolio/single_project.html", {"project": project})


def single_blog(request, slug):
    blog = Blogs.objects.get(slug=slug)
    return render(request, "portfolio/single_blog.html", {"blog": blog})


def contact(request):
    if request.method == "POST":
        sender_name = request.POST["name"]
        sender_email = request.POST["email2"]
        sender_phone = request.POST["phone"]
        message = request.POST["message2"]
        contact = Contact.objects.create(
            name=sender_name, email=sender_email, phone=sender_phone, message=message
        )
        contact.save()
        messages.success(
            request, "Thank you for your message. We will get back to you soon."
        )
        return redirect("/")
    return render(request, "portfolio/contact.html")


def skillsandtools(request):
    pass
