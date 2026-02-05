"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from catalogo import views
# --- NUEVOS IMPORTS PARA FOTOS ---
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('sedes/', views.sedes, name='sedes'),
    path('lentes/', views.catalogo, name='catalogo'),
    path('lentes/<int:producto_id>/', views.detalle_producto, name='detalle_producto'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('setup-secreto/', views.setup_datos, name='setup_datos'),
]

# --- ESTO PERMITE VER LAS FOTOS MIENTRAS DESARROLLAS ---
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)