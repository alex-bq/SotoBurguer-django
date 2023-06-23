from django.shortcuts import render

# Create your views here.
def menu(request):
    return render(request,"menu.html")

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