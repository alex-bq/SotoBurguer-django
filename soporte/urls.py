from django.urls import path
from . import views


urlpatterns = [
    path('',views.soporte),
    path('registrarSoporte', views.registrarSoporte)
    
]