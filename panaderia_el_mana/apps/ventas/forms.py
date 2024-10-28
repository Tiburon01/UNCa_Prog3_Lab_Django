from django import forms
from .models import Venta, Mayorista, Empleado, Producto

class VentaForm(forms.ModelForm):
    class Meta:
        model = Venta
        fields = [
            'tipo_venta',
            'forma_pago',
            'tipo_comprobante',
            'numero_comprobante',
            'observaciones',
            # 'empleado',
            # 'mayorista',
            # 'producto',
        ]

# class MayoristaForm(forms.ModelForm):
#     class Meta:
#         model = Mayorista
#         fields = [

#         ]

# class EmpleadoForm(forms.ModelForm):
#     class Meta:
#         model = Empleado
#         fields = [

#         ]

# class ProductoForm(forms.ModelForm):
#     class Meta:
#         model = Producto
#         fields = [

#         ]