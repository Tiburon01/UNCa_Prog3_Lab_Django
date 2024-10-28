from django.urls import path
from .views import lista_ventas, registrar_venta

app_name='ventas'

urlpatterns = [
    # path('', , name='home'),
    path('', lista_ventas, name='home'),
    path('registrar/', registrar_venta, name='registrar')
]
