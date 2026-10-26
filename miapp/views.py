from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from .models import Producto


class HomeView(TemplateView):
    template_name = 'miapp/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['productos'] = Producto.objects.all()

        context['productos_destacados'] = [
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

        context['nombre'] = 'Tienda Libre'
        context['productos_recientes'] = Producto.objects.order_by('-id')[:6]

        return context


class CatalogoView(ListView):
    model = Producto
    template_name = 'miapp/catalogo.html'
    context_object_name = 'productos'
    paginate_by = 6


class ProductoDetailView(DetailView):
    model = Producto
    template_name = 'miapp/detalle.html'
    context_object_name = 'producto'


def productos(request):
    productos = Producto.objects.all()

    return render(request, 'miapp/productos.html', {
        'productos': productos
    })


def acerca_de_mi(request):
    return render(request, 'miapp/acerca-de-mi.html')
