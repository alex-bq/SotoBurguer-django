from django.shortcuts import render
from .models import Feedback

# Create your views here.

def index(request):
    return render(request,"index.html")

def menu(request):
    return render(request,"menu.html")