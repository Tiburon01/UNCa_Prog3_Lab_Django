from django.shortcuts import render
from .models import Venta, Caja
from .forms import VentaForm

# Create your views here.

def lista_ventas(request):
    ventas = Venta.objects.all() #.select_related('pk')

    return render(request, 'lista_ventas.html', {'ventas': ventas})

def registrar_venta(request):
    if request.method == 'POST':
        form = VentaForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = VentaForm()
    return render(request, 'registrar_ventas.html', {'form': form})