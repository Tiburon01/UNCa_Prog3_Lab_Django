from django.urls import path
from .views import lista_ventas, registrar_venta

app_name='ventas'

urlpatterns = [
    # path('', , name='home'),
    path('lista/', lista_ventas, name='lista'),
    path('', registrar_venta, name='home')
]
