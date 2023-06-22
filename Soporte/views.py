from django.shortcuts import render
from .models import Feedback

# Create your views here.

def index(request):
    return render(request,"index.html")

def menu(request):
    return render(request,"menu.html")

def nosotros(request):
    return render(request,"Nosotros.html")

def locales(request):
    return render(request,"Locales.html")