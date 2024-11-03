from django.contrib import messages
from django.shortcuts import render, redirect
from .models import Venta, DetalleVenta, Producto
from .forms import VentaForm, DetalleVentaForm, DetalleVentaFormSet

# Lista de ventas

def lista_ventas(request):
    ventas = Venta.objects.all() #.select_related('pk')

    return render(request, 'lista_ventas.html', {'ventas': ventas})

def lista_productos(request):
    productos = Producto.objects.all() #.select_related('pk')

    return render(request, 'lista_ventas.html', {'productos': productos})

#Registro de formularios

def registrar_venta(request):
    ventas = Venta.objects.all() #.select_related('pk')
    productos = Producto.objects.all() #.select_related('pk')

    if request.method == 'POST':
        form = VentaForm(request.POST, request.FILES)
        formset = DetalleVentaFormSet(request.POST, request.FILES) # instance=nueva_venta   colocarlo aqui hace que intente relacionarse con el id, pero nueva_venta aun no fue guardada en la BD por ende no tiene id.

        if form.is_valid() and formset.is_valid():
            nueva_venta = form.save(commit=False) # Guarda los datos del formulario en el objeto nueva_venta. Esto permite hacer cambios adicionales antes de guardar los datos en la base de datos.
            detalle_venta = formset.save(commit=False)
                
            nueva_venta.save()
            for detalle in detalle_venta:
                detalle.venta = nueva_venta
                detalle.save()

            messages.success(request, 'Se ha agregado correctamente la venta {}'.format(nueva_venta, detalle_venta))
            return redirect(request.path)
    else:
        form = VentaForm()
        formset = DetalleVentaFormSet()
    return render(request, 'registrar_ventas.html', {'form': form, 'detalleForm': formset, 'ventas': ventas, 'productos': productos})