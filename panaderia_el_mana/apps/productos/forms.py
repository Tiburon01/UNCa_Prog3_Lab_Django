from django import forms
from .models import Producto

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = [
            'descripcion',
            'categoria',
            'stock',
            'precio',
        ]
        widgets = {
            'descripcion': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'categoria': forms.Select(attrs={
                'class': 'form-control'
            }),
            'stock': forms.NumberInput(attrs={
                'class': 'form-control'
            }),
            'precio': forms.NumberInput(attrs={
                'class': 'form-control'
            }),
        }

class ModificarProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = [
            'descripcion',
            'categoria',
            'stock',
            'precio',
        ]
        widgets = {
            'descripcion': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'categoria': forms.Select(attrs={
                'class': 'form-control'
            }),
            'stock': forms.NumberInput(attrs={
                'class': 'form-control'
            }),
            'precio': forms.NumberInput(attrs={
                'class': 'form-control'
            }),
        }