from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import *
from django.views import View
from django.views.generic import ListView
from django.core.mail import send_mail, BadHeaderError
from django.contrib import messages

# Create your views here.


def main(request):
    all_colleagues = Colleagues.objects.filter(is_approve = True)
    if request.method == 'POST':
        if request.FILES.get('image') == None:
            colleagues_name = request.POST['name']
            job_title = request.POST['jobtitle']
            workplace = request.POST['workplace']
            comment = request.POST['comment2']
            
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
        if  request.FILES['image'] != None:
            colleagues_name = request.POST['name']
            job_title = request.POST['jobtitle']
            workplace = request.POST['workplace']
            comment = request.POST['comment2']
            image = request.FILES['image']
            
            colleagues = Colleagues.objects.create(
                name=colleagues_name,
                job_title=job_title,
                workplace=workplace,
                comment=comment,
                image = image
            )
            colleagues.save()
            messages.success(
                request, "Thank you for your comment. I will approve to it soon."
            )
            return redirect("/")
        
    if len(all_colleagues) == 0:
        colleagues = 'Be the first to comment.'
        return render(request, "portfolio/portfolio.html", {"colleague": colleagues})
    return render(request, "portfolio/portfolio.html", {"colleagues": all_colleagues})


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
              