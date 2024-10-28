from django.contrib import admin
from .models import Venta, Caja, Empleado

# Register your models here.

admin.site.register(Venta)
admin.site.register(Caja)
admin.site.register(Empleado)