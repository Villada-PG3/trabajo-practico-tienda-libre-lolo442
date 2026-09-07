
from django.shortcuts import render
from .models import Producto


def home(request):
    productos = Producto.objects.all()

    productos_destacados = [
        {
            'nombre': 'martillo profesional',
            'marca': 'Stanley',
            'descripcion': 'Martillo profesional para trabajos de construcción y reparación.',
            'precio': 15000
        },
        {
            'nombre': 'licuadora',
            'marca': 'Philips',
            'descripcion': 'Licuadora ideal para preparar bebidas y comidas.',
            'precio': 45000
        },
        {
            'nombre': 'auriculares inalámbricos',
            'marca': 'Sony',
            'descripcion': 'Auriculares inalámbricos con excelente calidad de sonido.',
            'precio': 35000
        },
        {
            'nombre': 'sartén antiadherente',
            'marca': 'Tramontina',
            'descripcion': 'Sartén antiadherente para cocinar diferentes tipos de alimentos.',
            'precio': 28000
        },
        {
            'nombre': 'teclado mecánico',
            'marca': 'Logitech',
            'descripcion': 'Teclado cómodo y resistente para computadora.',
            'precio': 22000
        },
        {
            'nombre': 'pelota deportiva',
            'marca': 'Adidas',
            'descripcion': 'Pelota deportiva de gran calidad para entrenamiento.',
            'precio': 18000
        },
        {
            'nombre': 'producto sin precio',
            'marca': 'Genérica',
            'descripcion': 'Este producto todavía no tiene un precio definido.',
            'precio': None
        }
    ]

    return render(request, 'miapp/home.html', {
        'productos': productos,
        'productos_destacados': productos_destacados,
        'nombre': 'Tienda Libre'
    })


def productos(request):
    productos = Producto.objects.all()

    return render(request, 'miapp/productos.html', {
        'productos': productos
    })


def acerca_de_mi(request):
    return render(request, 'miapp/acerca-de-mi.html')

def catalogo(request):
    productos = Producto.objects.all()
    return render(request, "miapp/catalogo.html", {"productos": productos})