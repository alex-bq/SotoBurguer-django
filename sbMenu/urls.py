from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('',views.menu),
    path('hamburguesa/<int:id>/',  views.ver_hamburguesa),
    path('gestionburger/', views.gestionBurger),
    path('agregarburger/',views.agregarHamburguesa),
    path('carrito/',views.carrito),
    path('ventas/',views.listarVentas),
    path('agregar_al_carrito/<int:hamburguesa_id>/', views.agregar_al_carrito),
    path('carrito/eliminar/<int:item_id>/', views.eliminar_item_carrito),
    path('carrito/guardar_compra/', views.guardar_compra),
    path('editarBurguer/<id>/', views.editarBurguer),
    path('eliminarBurguer/<id>', views.eliminarBurguer),
] 