from django.test import TestCase
from django.urls import reverse


class ProductosTemplateTests(TestCase):
    def test_productos_page_renders(self):
        response = self.client.get(reverse('productos'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'miapp/productos.html')
