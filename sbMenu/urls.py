from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('',views.menu),
    path('hamburguesa/<int:id>/',  views.ver_hamburguesa),
    path('gestionburger/', views.gestionBurger),
    path('agregarburger/',views.agregarHamburguesa),
] 