from django.contrib import messages
from django.shortcuts import render,redirect, get_object_or_404
from .models import Producto
from .forms import ProductoForm, ModificarProductoForm
from django.contrib.auth.decorators import login_required, permission_required

# Create your views here.

@login_required
def lista_productos(request):
    productos = Producto.objects.filter(estado='ACTIVO').order_by('id_producto')
    return render(request, 'lista_productos.html', {'productos': productos})

@login_required
def registrar_productos(request):
    productos = Producto.objects.filter(estado='ACTIVO').order_by('id_producto')

    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES)
        if form.is_valid():
            productos = form.save(commit=False)

            productos.save()
            messages.success(request, 'Se ha registrado correctamente el producto')
            return redirect(request.path)
        else:
            messages.error(request, 'Hay errores! No se ha podido registrar el producto')
    else:
        form = ProductoForm()
    return render(request, 'registrar_productos.html', {'form': form, 'productos': productos})

@login_required
def modificar_productos(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == 'POST':
        form_mod = ModificarProductoForm(request.POST, request.FILES, instance=producto)
        if form_mod.is_valid():
            producto = form_mod.save(commit=False)

            producto.save()
            messages.success(request, 'Se ha modificado correctamente el producto')
            return redirect('productos:home')
        else:
            messages.error(request, 'Hay errores! No se ha podido modificar el producto')
    else:
        form_mod = ProductoForm(instance=producto)
    return render(request, 'modificar_productos.html', {'form_mod': form_mod})

@login_required
def eliminar_productos(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == 'POST':
        producto.estado = 'INACTIVO'
        producto.save()

        messages.success(request, "El producto ha sido eliminado exitosamente.")
        return redirect('productos:home')
    else:
        messages.error(request, "El producto no pudo ser eliminado.")
        return redirect('productos:home')