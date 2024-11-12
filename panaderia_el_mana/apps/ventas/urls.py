from django.urls import path
from . import views

app_name='ventas'

urlpatterns = [
    path('lista/', views.lista_ventas, name='lista'),
    path('detalle/<int:pk>/', views.lista_detalles, name='detalle'),
    path('', views.registrar_venta, name='home'),
    path('modificar/<int:pk>/', views.modificar_venta, name='modificar'),
    path('anular/<int:pk>/', views.anular_ventas, name='anular'),
]
