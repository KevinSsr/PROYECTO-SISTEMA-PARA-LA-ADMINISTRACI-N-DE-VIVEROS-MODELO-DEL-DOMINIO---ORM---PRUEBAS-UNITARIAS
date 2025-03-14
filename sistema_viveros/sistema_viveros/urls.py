from django.urls import path
from django.http import HttpResponse
from django.urls import include


def home(request):
    return HttpResponse("Bienvenido a Sistema Viveros")

urlpatterns = [
    path("", home, name="home"),  
    path("productores/", include("viveros.productores.urls")),  
]
