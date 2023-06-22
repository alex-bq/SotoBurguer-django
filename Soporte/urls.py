from django.urls import path
from . import views


urlpatterns = [
    path('',views.index),
    path('menu/',views.menu),
    path('nosotros/',views.nosotros),
    path('locales/',views.locales),
    path('soporte/',views.soporte),
    path('stobger/', views.stobger),
]