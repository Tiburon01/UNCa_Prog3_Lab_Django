"""
URL configuration for panaderia_el_mana project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from .views import homeView
# from apps.ventas import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homeView, name='home'),
    path('ventas/', include('apps.ventas.urls', namespace='ventas')),
    path('usuarios/', include('apps.usuarios.urls', namespace='usuarios')),
    path('productos/', include('apps.productos.urls', namespace='productos')),

    # path('ventas/', views.lista_ventas, name='lista_ventas'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
