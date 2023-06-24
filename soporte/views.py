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
    return redirect('/soporte/gestion/')

def eliminacionFeedback(request,id):
    feedbacks = feedback.objects.get(id=id)
    feedbacks.delete()
    return redirect('/')
    

def soporte(request):
    if request.method is not "POST":
        tipos= tipoMensaje.objects.all();
        ciudades= ciudad.objects.all()
        context={'tipo':tipos,'ciudad':ciudades}
        return render(request,'soporte/Agregar.html',context)
    else :
        nombre=request.POST["nombre"]
        correo=request.POST["correo"]
        tipoMensaje=request.POST["tipoMensaje"]
        tipoMensaje=request.POST["tipoMensaje"]
        comentario=request.POST["comentario"]
        activo="1"

        objTipoMensaje=tipoMensaje.objects.get(id_tipo_mensaje = tipoMensaje)
        obj=Usuario.objects.create ( nombre=nombre,
                                    correo=correo,
                                    tipoMensaje=tipoMensaje,
                                    tipoMensaje=tipoMensaje,
                                    comentario=comentario,
                                    activo=1 )
        obj.save()
        context={'mensaje':"Ok, datos grabados..."}
        return render (request, 'soporte/Agregar.html', context)


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


        

