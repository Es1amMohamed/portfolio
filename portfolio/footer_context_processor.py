from .models import *


def my_portfolio(request):
    my_portfolio = Portfolio.objects.first()
    about = AboutMe.objects.last()
    context = {
        "my_portfolio": my_portfolio,
        "about": about,
    }

    return context
