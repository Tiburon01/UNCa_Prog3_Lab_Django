from decimal import Decimal
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .models import Venta, DetalleVenta
from apps.productos.models import Producto
from .forms import VentaForm, DesVentaForm, ModificarVentaForm, DetalleVentaFormSet
from django.core.serializers import serialize
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
import json

# Lista de ventas

@login_required(login_url='usuarios:login')
def lista_ventas(request):
    ventas = Venta.objects.filter(estado='REGISTRADA').order_by('-id_venta')
    return render(request, 'lista_ventas.html', {'ventas': ventas})

@login_required(login_url='usuarios:login')
def lista_detalles(request, pk):
    venta = get_object_or_404(Venta, pk=pk)
    form = DesVentaForm(instance=venta)
    detalles = DetalleVenta.objects.all().filter(venta=venta)
    return render(request, 'lista_detalles.html', {'detalles': detalles, 'form':form})

# Registro de formularios

def productos_json(request):
    productos = Producto.objects.all().values('id_producto', 'descripcion', 'categoria', 'precio')
    productos_list = list(productos)  # Convertir QuerySet a una lista de diccionarios
    return JsonResponse(productos_list, safe=False)

@login_required(login_url='usuarios:login')
def registrar_venta(request):
    ventas = Venta.objects.filter(estado='REGISTRADA').order_by('-id_venta')
    productos = Producto.objects.all()
    if request.method == 'POST':
        form = VentaForm(request.POST, request.FILES)
        if form.is_valid():
            nueva_venta = form.save(commit=False) # Guarda los datos del formulario en el objeto nueva_venta. Esto permite hacer cambios adicionales antes de guardar los datos en la base de datos.
            # validaciones de ventas
            nueva_venta.save()
            formset = DetalleVentaFormSet(request.POST, request.FILES, instance=nueva_venta) # instance=nueva_venta   colocarlo aqui hace que intente relacionarse con el id, pero nueva_venta aun no fue guardada en la BD por ende no tiene id.
            if formset.is_valid():
                detalle_venta = formset.save(commit=False)
                precio_total = 0
                # validaciones de productos
                for detalle in detalle_venta:
                    for producto in productos:
                        if producto.id_producto == detalle.producto.id_producto:
                            subtotal = detalle.cantidad * producto.precio  # Calcula subtotal del producto
                            precio_total += subtotal  # Agrega el subtotal al precio total
                    detalle.save()  # Guarda el detalle en la base de datos
                nueva_venta.precio_total = precio_total  # Asigna el precio total calculado a la venta
                nueva_venta.save()  # Guarda la venta con su nuevo valor de precio_total en la base de datos
                messages.success(request, 'Se ha agregado correctamente la venta {}'.format(nueva_venta, detalle_venta))
                return redirect(request.path)
            else:
                messages.error(request, 'Hay errores en los productos agregados.')
        else:
            formset = DetalleVentaFormSet()
    else:
        form = VentaForm()
        formset = DetalleVentaFormSet()
    return render(request, 'registrar_ventas.html', {'form': form, 'detalleForm': formset, 'ventas': ventas})

# Modificacion de formularios

@login_required(login_url='usuarios:login')
def modificar_venta(request, pk):
    venta = get_object_or_404(Venta, pk=pk)
    productos = Producto.objects.all()
    if request.method == 'POST':
        form_mod = ModificarVentaForm(request.POST, request.FILES, instance=venta)
        formset_mod = DetalleVentaFormSet(request.POST, instance=venta)
        if form_mod.is_valid():
            form_mod.save()
            if formset_mod.is_valid():
                detalle_venta = formset_mod.save(commit=False)
                precio_total = 0
                # validaciones de productos
                for detalle in detalle_venta:
                    for producto in productos:
                        if producto.id_producto == detalle.producto.id_producto:
                            subtotal = detalle.cantidad * producto.precio  # Calcula subtotal del producto
                            precio_total += subtotal  # Agrega el subtotal al precio total
                    detalle.save()  # Guarda el detalle en la base de datos
                form_mod.precio_total = precio_total  # Asigna el precio total calculado a la venta
                form_mod.save()  # Guarda la venta con su nuevo valor de precio_total en la base de datos

                # formset_mod.save()
                messages.success(request, 'Se ha actualizado correctamente la venta')
                return redirect(reverse('ventas:home'))
            else:
                messages.error(request, 'No se ha actualizado correctamente la venta')
                messages.error(request, f'Error en el formulario de venta: {form_mod.errors}')
                messages.error(request, f'Error en el formset de detalle: {formset_mod.errors}')
    else:
        form_mod = ModificarVentaForm(instance=venta)
        formset_mod = DetalleVentaFormSet(instance=venta)
    return render(request, 'modificar_ventas.html', {'form_mod': form_mod, 'formset_mod': formset_mod, 'venta': venta})

# Eliminacion de formularios

@login_required(login_url='usuarios:login')
def anular_ventas(request, pk):
    venta = get_object_or_404(Venta, pk=pk)
    if request.method == 'POST':
        venta.estado = 'CANCELADA'
        venta.save()

        messages.success(request, "La venta ha sido anulada exitosamente.")
        return redirect('ventas:home')
    else:
        messages.error(request, "La venta no pudo ser anulada.")
        return redirect('ventas:home')