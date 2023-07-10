from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages

# Create your views here.
def gestion(request):
    tipos= tipoMensaje.objects.all()
    ciudades= ciudad.objects.all()
    feedbackLista = feedback.objects.all()
    return render(request, "gestion.html",{"feedback" : feedbackLista,
                                           "tipo" : tipos,
                                           "ciudad" : ciudades})

def registrarFeedback(request):
    nombre=request.POST['nombre']
    correo=request.POST['email']
    comentario=request.POST['mensaje']

    feedbacks = feedback.objects.create(
        nombre=nombre, correo=correo, comentario=comentario)
    messages.success(request, "Mensaje registrado correctamente")
    return redirect('/soporte')

def eliminarFeedback(request,id):
    feedbacks = feedback.objects.get(id=id)
    feedbacks.delete()
    messages.success(request, "Mensaje borrado exitosamente :$")
    return redirect('/soporte/gestion/')
    
def soporte(request):
    return render(request, "soporte.html")




        

