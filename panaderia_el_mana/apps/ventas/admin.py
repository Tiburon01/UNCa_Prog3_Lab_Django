from django.contrib import admin
from .models import Empleado, Mayorista, Venta, DetalleVenta, Caja

# Register your models here.

admin.site.register(Empleado)
admin.site.register(Mayorista)
# admin.site.register(Producto)
admin.site.register(Venta)
admin.site.register(DetalleVenta)
admin.site.register(Caja)