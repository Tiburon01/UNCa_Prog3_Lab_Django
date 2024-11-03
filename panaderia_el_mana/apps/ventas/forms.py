from django.forms import inlineformset_factory
from django import forms
from .models import Venta, DetalleVenta

class VentaForm(forms.ModelForm):
    class Meta:
        model = Venta
        fields = [
            'tipo_venta',
            'forma_pago',
            'tipo_comprobante',
            'numero_comprobante',
            'observaciones',
            'precio_total',
            'empleado',
            'mayorista',
            # 'producto',
        ]

class DetalleVentaForm(forms.ModelForm):
    class Meta:
        model = DetalleVenta
        fields = [
            # 'venta',
            'producto',
            'cantidad',
        ]

DetalleVentaFormSet = inlineformset_factory(Venta, DetalleVenta, form=DetalleVentaForm, extra=1, can_delete=True)
# crea un formset en línea para manejar instancias de DetalleVenta hasta el numero indicado en extra # permite que todos los formularios de DetalleVenta se vinculen automáticamente a una instancia específica de Venta.


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