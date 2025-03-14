from django.urls import path
from .views import listar_productores

urlpatterns = [
    path("productores/", listar_productores, name="listar_productores"),
]