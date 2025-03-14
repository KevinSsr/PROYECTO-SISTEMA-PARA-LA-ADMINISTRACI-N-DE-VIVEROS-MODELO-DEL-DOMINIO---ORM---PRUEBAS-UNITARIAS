from django.shortcuts import render
from django.http import JsonResponse
from .models import Productor

def listar_productores(request):
    productores = list(Productor.objects.values())
    return JsonResponse({"productores": productores})