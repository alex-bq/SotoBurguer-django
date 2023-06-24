from django.shortcuts import render, redirect
from .models import *


# Create your views here.



def soporte(request):
    if request.method is not "POST":
        tipos= tipoMensaje.objects.all();
        ciudades= ciudad.objects.all()
        context={'tipo':tipos,'ciudad':ciudades}
        return render(request,'soporte.html',context)
    
def registrarSoporte(request):
    nombre=request.POST['txtNombre']
    correo=request.POST['txtCorreo']
    tipoMensa=request.POST['txtTipo']
    ciudad=request.POST['txtCiudad']
    mensaje=request.POST['txtMensaje']

    mensajeSoporte=feedback.objects.create(
        nombre=nombre, correo=correo, tipoMensa=tipoMensa, ciudad=ciudad, mensaje=mensaje
    )
    return redirect('/')

def crud(request):
    soporte = Soporte.objects.all()
    context = {'soporte': soporte}
    return render(request, 'soporte/soporte.html', context)

