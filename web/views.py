from django.shortcuts import render

# Create your views here.
 
def index(request):
    return render(request,"index.html")

def nosotros(request):
    return render(request,"Nosotros.html")

def locales(request):
    return render(request,"Locales.html")