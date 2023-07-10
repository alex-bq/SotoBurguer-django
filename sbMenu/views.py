from django.shortcuts import render, get_object_or_404
from .models import *
from .forms import *
\


def menu(request):
    hamburguesas = hamburguesa.objects.all()
    context = {
        'hamburguesas': hamburguesas
    }
    return render(request, 'menu.html', context)

def ver_hamburguesa(request, id):
    hamburguesa_obj = get_object_or_404(hamburguesa, id=id)
    context = {'hamburguesa': hamburguesa_obj}
    return render(request, 'ver_hamburguesa.html', context)


def gestionBurger(request):
    hamburguesas = hamburguesa.objects.all()
    return render(request, "adminBurger/gestionBurger.html",{"hamburguesa" : hamburguesas,})

def agregarHamburguesa(request):

    data = {
        'form' : hamburguesaForm()
    }

    return render(request,"adminBurger/agregarBurger.html",data)