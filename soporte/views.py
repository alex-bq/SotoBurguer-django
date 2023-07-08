from django.shortcuts import render, redirect
from .models import *


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
    return redirect('/soporte')

def eliminarFeedback(request,id):
    feedbacks = feedback.objects.get(id=id)
    feedbacks.delete()
    return redirect('/soporte/gestion/')
    
def soporte(request):
    return render(request, "soporte.html")




        

