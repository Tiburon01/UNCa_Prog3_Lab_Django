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
        widgets = {
            'tipo_venta': forms.Select(attrs={
                'class': 'form-control'
            }),
            'forma_pago': forms.Select(attrs={
                'class': 'form-control'
            }),
            'tipo_comprobante': forms.Select(attrs={
                'class': 'form-control'
            }),
            'numero_comprobante': forms.NumberInput(attrs={
                'class': 'form-control'
            }),
            'observaciones': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3
            }),
            'precio_total': forms.NumberInput(attrs={
                'class': 'form-control',
                'disabled': 'disabled'
            }),
            'empleado': forms.Select(attrs={
                'class': 'form-select'
            }),
            'mayorista': forms.Select(attrs={
                'class': 'form-select'
            }),
        }

class DesVentaForm(forms.ModelForm):
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
        widgets = {
            'tipo_venta': forms.Select(attrs={
                'class': 'form-control',
                'disabled': 'disabled'
            }),
            'forma_pago': forms.Select(attrs={
                'class': 'form-control',
                'disabled': 'disabled'
            }),
            'tipo_comprobante': forms.Select(attrs={
                'class': 'form-control',
                'disabled': 'disabled'
            }),
            'numero_comprobante': forms.NumberInput(attrs={
                'class': 'form-control',
                'disabled': 'disabled'
            }),
            'observaciones': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'disabled': 'disabled'
            }),
            'precio_total': forms.NumberInput(attrs={
                'class': 'form-control',
                'disabled': 'disabled'
            }),
            'empleado': forms.Select(attrs={
                'class': 'form-select',
                'disabled': 'disabled'
            }),
            'mayorista': forms.Select(attrs={
                'class': 'form-select',
                'disabled': 'disabled'
            }),
        }


class DetalleVentaForm(forms.ModelForm):
    class Meta:
        model = DetalleVenta
        fields = [
            # 'venta',
            'producto',
            'cantidad',
        ]
        widgets = {
            'producto': forms.Select(attrs={
                'class': 'form-select'
            }),
            'cantidad': forms.NumberInput(attrs={
                'class': 'form-control'
            }),
        }

class ModificarVentaForm(forms.ModelForm):
    class Meta:
        model = Venta
        fields = [
            'tipo_venta',
            'forma_pago',
            'tipo_comprobante',
            'observaciones',
            'precio_total',
            'empleado',
            'mayorista',            
        ]
        widgets = {
            'tipo_venta': forms.Select(attrs={
                'class': 'form-control'
            }),
            'forma_pago': forms.Select(attrs={
                'class': 'form-control'
            }),
            'tipo_comprobante': forms.Select(attrs={
                'class': 'form-control'
            }),
            'observaciones': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3
            }),
            'precio_total': forms.NumberInput(attrs={
                'class': 'form-control'

            }),
            'empleado': forms.Select(attrs={
                'class': 'form-select'
            }),
            'mayorista': forms.Select(attrs={
                'class': 'form-select'
            }),
        }

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