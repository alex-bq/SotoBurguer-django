from django.urls import path
from . import views


urlpatterns = [
    path('',views.index),
    path('nosotros/',views.nosotros),
    path('locales/',views.locales),
    path('registro/', views.registro),
    path('login/', views.login_view),

]