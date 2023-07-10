from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm,CustomAuthenticationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages


# Create your views here.
 
def index(request):
    return render(request,"index.html")

def nosotros(request):
    return render(request,"Nosotros.html")

def locales(request):
    return render(request,"Locales.html")




def registro(request):
    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            login(request, user)
            messages.success(request, "Registrado correctamente")
            return redirect(to="/")
        else:
            for field_name, errors in formulario.errors.items():
                for error in errors:
                    messages.error(request, error)
    else:
        formulario = CustomUserCreationForm()

    return render(request, 'registration/registro.html', {'form': formulario})




def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(to="/")  
        else:
            messages.error(request, "Datos incorrectos")
            return render(request,'registration/login.html')
    else:
        return render(request, 'registration/login.html')
