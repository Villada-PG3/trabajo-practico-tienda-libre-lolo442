from django.shortcuts import render
from .models import Producto


def home(request):
    productos = Producto.objects.all()

    return render(request, 'miapp/home.html', {
        'productos': productos
    })


def productos(request):
    productos = Producto.objects.all()

    return render(request, 'miapp/productos.html', {
        'productos': productos
    })


def acerca_de_mi(request):
    return render(request, 'miapp/acerca-de-mi.html')