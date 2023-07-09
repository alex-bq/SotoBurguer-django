from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('',views.menu),
    path('stobger/', views.stobger),
    path('stobger2/', views.stobger2),
    path('stobger3qsos/', views.stobger3qsos),
    path('stobgeregg/', views.stobgeregg),
    path('stobgerfries/', views.stobgerfries),
    path('stobgerhilo/', views.stobgerhilo),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)