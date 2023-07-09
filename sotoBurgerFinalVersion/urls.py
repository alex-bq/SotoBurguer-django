
from django.contrib import admin
from django.conf import settings
from django.views.static import serve
from django.urls import path,include,re_path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include("web.urls")),
    path('soporte/',include("soporte.urls")),
    path('menu/',include("sbMenu.urls")),
    path('cuenta/', include('django.contrib.auth.urls')),
    
]

urlpatterns += [
    re_path(r'^media/(?P<path>.*)$', serve, {
        'document_root' :settings.MEDIA_ROOT,
    })
]
