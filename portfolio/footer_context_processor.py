from .models import *


def my_portfolio(request):
    my_portfolio = Portfolio.objects.first()

    return {"my_portfolio": my_portfolio}
