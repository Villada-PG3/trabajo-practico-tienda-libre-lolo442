from django.test import TestCase
from django.urls import reverse

from .models import Producto


class ProductosTemplateTests(TestCase):
    def test_productos_page_renders(self):
        response = self.client.get(reverse('productos'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'miapp/productos.html')


class HomeAndCatalogoViewTests(TestCase):
    def crear_producto(self, nombre):
        return Producto.objects.create(
            nombre=nombre,
            marca='Marca',
            precio='10.00',
        )

    def test_home_shows_six_most_recent_products(self):
        productos = [
            self.crear_producto(f'Producto {numero}')
            for numero in range(7)
        ]

        response = self.client.get(reverse('home'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'miapp/home.html')
        self.assertEqual(
            list(response.context['productos_recientes']),
            list(reversed(productos[-6:])),
        )

    def test_catalogo_lists_all_products(self):
        productos = [
            self.crear_producto('Producto A'),
            self.crear_producto('Producto B'),
        ]

        response = self.client.get(reverse('catalogo'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'miapp/catalogo.html')
        self.assertQuerySetEqual(
            response.context['productos'],
            productos,
            ordered=False,
        )
