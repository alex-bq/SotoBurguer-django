from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from .forms import *
from datetime import datetime
from django.contrib import messages


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
    return render(request, "adminBurger/gestionBurger.html",{"hamburguesa" : hamburguesas})

def agregarHamburguesa(request):
    data = {
        'form' : hamburguesaForm()
    }
    return render(request,"adminBurger/agregarBurger.html",data)

def carrito(request):
    carrito_items = carritoItem.objects.all()
    total = sum(item.precio for item in carrito_items)
    cantidad = len(carrito_items)
    return render(request, 'carrito.html', {'carrito': carrito_items, 'total': total, 'cantidad': cantidad})

def agregar_al_carrito(request, hamburguesa_id):
    hamburguesa_item = hamburguesa.objects.get(id=hamburguesa_id)
    carrito_item = carritoItem(hamburguesa=hamburguesa_item, nombre=hamburguesa_item.nombre, precio=hamburguesa_item.precio)
    carrito_item.save()
    return redirect('/menu/')

def guardar_compra(request):
    carrito_items = carritoItem.objects.all()
    total = sum(item.precio for item in carrito_items)

    # Obtén la fecha actual
    fecha_actual = datetime.now()

    # Crea la instancia de Compra y guarda los detalles de la venta
    Compra = compra(total=total, fecha=fecha_actual)
    Compra.save()

    # Guarda la cantidad de hamburguesas compradas
    cantidad = len(carrito_items)
    ompra.cantidad = cantidad
    Compra.save()

    # Otros detalles de la venta
    # compra.detalle = ...

    # Vacía el carrito
    carrito_items.delete()

    return redirect('/menu/')

def agregarHamburguesa(request):

    data = {
        'form' : hamburguesaForm()
    }

    if request.method == 'POST':

        formulario = hamburguesaForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Guardado correctamente")
            data["mensaje"] = "Guardado correctamente"
            return redirect(to="/menu/gestionburger/")
        else:
            data["form"] = formulario
 
    return render(request,"adminBurger/agregarBurger.html",data)

def editarBurguer (request, id):

    hamburguesas = get_object_or_404(hamburguesa, id=id)

    data = {
        'form': hamburguesaForm(instance=hamburguesas)
    }

    if request.method == 'POST':
        formulario = hamburguesaForm(data=request.POST, instance=hamburguesas, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Editado correctamente")
            data["mensaje"] = "Editado correctamente"
            return redirect(to="/menu/gestionburger/")
        data["form"] = formulario


    return render(request,"adminBurger/agregarBurger.html", data)

def eliminarBurguer (request, id):
    
    hamburguesas = get_object_or_404(hamburguesa, id=id)
    hamburguesas.delete()
    messages.success(request, "Eliminado correctamente")
    return redirect(to="/menu/gestionburger/")




