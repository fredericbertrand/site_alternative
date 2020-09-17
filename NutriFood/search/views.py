from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse("Hey ! tu es sur l'index de l'application search du projet NutriFood.")
    