from django.urls import path
from . import views
from .views import *

app_name = "portfolio"

urlpatterns = [
    path("", views.main, name="main"),
]
