from django.shortcuts import render
from .models import Feedback

# Create your views here.

def soporte(request):
    return render(request, "soporte.html")

