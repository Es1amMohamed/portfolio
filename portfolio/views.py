from django.shortcuts import render

# Create your views here.


def main(request):
    return render(request, "portfolio/portfolio.html")


def translate(request):
    return render(request, "portfolio/portfolio2.html")
