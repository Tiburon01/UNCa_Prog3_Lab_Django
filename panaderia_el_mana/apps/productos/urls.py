from django.urls import path
from apps.productos import views

app_name = 'productos'

urlpatterns = [
    path('', views.registrar_productos, name='home'),
    path('lista/', views.lista_productos, name='lista'),
    path('modificar/<int:pk>/', views.modificar_productos, name='modificar'),
    path('eliminar/<int:pk>/', views.eliminar_productos, name='eliminar'),
]