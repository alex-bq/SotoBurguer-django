from django.urls import path
from . import views


urlpatterns = [
    path('',views.soporte),
    path('gestion/',views.gestion),
    path('registrarFeedback/',views.registrarFeedback),
    path('eliminarFeedback/<id>',views.eliminarFeedback)
    
]