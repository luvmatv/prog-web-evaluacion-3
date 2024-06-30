from django.shortcuts import render, get_object_or_404, redirect
from .models import Producto, CarritoItem
from .forms import ProductoForm, CarritoItemForm

def index(request):
    productos = Producto.objects.all()
    return render(request, 'turismo/index.html', {'productos': productos})

def producto_lista(request):
    productos = Producto.objects.all()
    return render(request, 'turismo/producto_lista.html', {'productos': productos})

def producto_detalle(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    return render(request, 'turismo/producto_detalle.html', {'producto': producto})

def producto_crear(request):
    if request.method == "POST":
        form = ProductoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('producto_lista')
    else:
        form = ProductoForm()
    return render(request, 'turismo/producto_form.html', {'form': form})

def producto_editar(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == "POST":
        form = ProductoForm(request.POST, request.FILES, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('producto_lista')
    else:
        form = ProductoForm(instance=producto)
    return render(request, 'turismo/producto_form.html', {'form': form})

def producto_eliminar(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == "POST":
        producto.delete()
        return redirect('producto_lista')
    return render(request, 'turismo/producto_eliminar.html', {'producto': producto})

def carrito_lista(request):
    carrito_items = CarritoItem.objects.all()
    return render(request, 'turismo/carrito_lista.html', {'carrito_items': carrito_items})

def carrito_agregar(request):
    if request.method == "POST":
        form = CarritoItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('carrito_lista')
    else:
        form = CarritoItemForm()
    return render(request, 'turismo/carrito_form.html', {'form': form})

def carrito_editar(request, pk):
    carrito_item = get_object_or_404(CarritoItem, pk=pk)
    if request.method == "POST":
        form = CarritoItemForm(request.POST, instance=carrito_item)
        if form.is_valid():
            form.save()
            return redirect('carrito_lista')
    else:
        form = CarritoItemForm(instance=carrito_item)
    return render(request, 'turismo/carrito_form.html', {'form': form})

def carrito_eliminar(request, pk):
    carrito_item = get_object_or_404(CarritoItem, pk=pk)
    if request.method == "POST":
        carrito_item.delete()
        return redirect('carrito_lista')
    return render(request, 'turismo/carrito_eliminar.html', {'carrito_item': carrito_item})
