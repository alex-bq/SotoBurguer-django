from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
# Create your views here.
 
def index(request):
    return render(request,"index.html")

def nosotros(request):
    return render(request,"Nosotros.html")

def locales(request):
    return render(request,"Locales.html")

def registro(request):
    data = {
        'form': CustomUserCreationForm()
    }

    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            login(request, user)
            messages.success(request, "Registrado correctamente")
            return redirect(to="/")
        data["form"] = formulario
    return render(request, 'registration/registro.html', data)