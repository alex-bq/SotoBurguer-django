from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('',views.menu),
    path('hamburguesa/<int:id>/',  views.ver_hamburguesa),
    path('gestionburger/', views.gestionBurger),
    path('agregarburger/',views.agregarHamburguesa),
<<<<<<< HEAD
    path('carrito/',views.carrito),
     path('agregar_al_carrito/<int:hamburguesa_id>/', views.agregar_al_carrito),
    path('guardar_compra/', views.guardar_compra),
=======
    path('editarBurguer/<id>/', views.editarBurguer),
    path('eliminarBurguer/<id>', views.eliminarBurguer),
>>>>>>> 35609c9f1bfe9af04bb72ed2a51f3320c2b24fc6
] 