from django.urls import path
from . import views


urlpatterns = [
    path('soporte',views.soporte, name='soporte'),
    path('registrarSoporte', views.registrarSoporte),
    path('crud', views.crud, name='crud'),
    path('Agregar', views.Agregar, name='Agregar'),

    
]