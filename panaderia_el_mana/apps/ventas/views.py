from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .models import Venta, DetalleVenta, Producto
from .forms import VentaForm, DetalleVentaForm, ModificarVentaForm, DetalleVentaFormSet

# Lista de ventas

def lista_ventas(request):
    ventas = Venta.objects.filter(estado='Registrada') #.select_related('pk')

    return render(request, 'lista_ventas.html', {'ventas': ventas})

def lista_productos(request):
    productos = Producto.objects.all() #.select_related('pk')

    return render(request, 'lista_ventas.html', {'productos': productos})

def lista_detalles(request, pk):
    venta = get_object_or_404(Venta, pk=pk)
    # detalles = DetalleVenta.objects.filter(id_venta=pk)
    detalles = DetalleVenta.objects.all().filter(venta=venta)

    return render(request, 'lista_detalles.html', {'detalles': detalles})

# Registro de formularios

def registrar_venta(request):
    ventas = Venta.objects.filter(estado='Registrada') #.select_related('pk')
    productos = Producto.objects.all() #.select_related('pk')

    if request.method == 'POST':
        form = VentaForm(request.POST, request.FILES)
        if form.is_valid():
            nueva_venta = form.save(commit=False) # Guarda los datos del formulario en el objeto nueva_venta. Esto permite hacer cambios adicionales antes de guardar los datos en la base de datos.
            # validaciones de ventas
            nueva_venta.save()
            formset = DetalleVentaFormSet(request.POST, request.FILES, instance=nueva_venta) # instance=nueva_venta   colocarlo aqui hace que intente relacionarse con el id, pero nueva_venta aun no fue guardada en la BD por ende no tiene id.
            if formset.is_valid():
                detalle_venta = formset.save(commit=False)
                # validaciones de productos
                for detalle in detalle_venta:
                    print(detalle_venta)
                    detalle.save()
                messages.success(request, 'Se ha agregado correctamente la venta {}'.format(nueva_venta, detalle_venta))
                return redirect(request.path)
            else:
                messages.error(request, 'Hay errores en los productos agregados.')
        else:
            formset = DetalleVentaFormSet()
    else:
        form = VentaForm()
        formset = DetalleVentaFormSet()
    return render(request, 'registrar_ventas.html', {'form': form, 'detalleForm': formset, 'ventas': ventas, 'productos': productos})

# Modificacion de formularios

def modificar_venta(request, pk):
    venta = get_object_or_404(Venta, pk=pk)
    if request.method == 'POST':
        form_mod = ModificarVentaForm(request.POST, request.FILES, instance=venta)
        if form_mod.is_valid():
            form_mod.save()
            formset_mod = DetalleVentaFormSet(request.POST, request.FILES, instance=venta)
            if formset_mod.is_valid():
                formset_mod.save()
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