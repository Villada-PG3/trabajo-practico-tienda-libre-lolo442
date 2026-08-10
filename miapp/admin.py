from django.contrib import admin
from django.utils.html import format_html
from .models import Categoria, Producto


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre',)


@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'marca', 'precio', 'categoria', 'mostrar_imagen')

    def mostrar_imagen(self, obj):
        if obj.imagen:
            return format_html(
                '<img src="{}" width="100" height="100" style="object-fit: contain;">',
                obj.imagen.url
            )
        return "Sin imagen"

    mostrar_imagen.short_description = 'Imagen'