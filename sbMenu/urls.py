from django.urls import path
from . import views

urlpatterns = [
    path('',views.menu),
    path('stobger/', views.stobger),
    path('stobger2/', views.stobger2),
    path('stobger3qsos/', views.stobger3qsos),
    path('stobgeregg/', views.stobgeregg),
    path('stobgerfries/', views.stobgerfries),
    path('stobgerhilo/', views.stobgerhilo),
    
]