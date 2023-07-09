from django.shortcuts import render
from .models import *

# Create your views here.
def menu(request):
    hamburguesas = hamburguesa.objects.all()
    context = {
        'hamburguesas': hamburguesas
    }
    return render(request, 'menu.html', context)

def stobger(request):
    return render(request, "stobger.html")

def stobger2(request):
    return render(request, "stobger2.html")

def stobger3qsos(request):
    return render(request, "stobger3qsos.html")

def stobgeregg(request):
    return render(request, "stobgeregg.html")

def stobgerfries(request):
    return render(request, "stobgerfries.html")
    
def stobgerhilo(request):
    return render(request, "stobgerhilo.html")