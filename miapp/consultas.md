
## 1 mostrar todos los productos

```python
Producto.objects.all()
```

muestra todos los productos registrados en la base de datos

## 2 productos con precio mayor a 500

```python
Producto.objects.filter(precio__gt=500)
```

busca productos cuyo precio sea mayor a 500

## 3 productos que no superan los 500

```python
Producto.objects.exclude(precio__gt=500)
```

muestra los productos cuyo precio no es mayor a 500

## 4 buscar un producto por ID

```python
Producto.objects.get(id=1)
```

busca el producto que tiene el ID 1. En este caso devuelve el producto "Termo"

## 5 ordenar productos por precio de menor a mayor

```python
Producto.objects.order_by("precio")
```

ordena los productos desde el menor precio hasta el mayor

## 6 ordenar productos por precio de mayor a menor

```python
Producto.objects.order_by("-precio")
```

ordena los productos desde el mayor precio hasta el menor

## 7 buscar productos cuyo nombre contenga "termo"

```python
Producto.objects.filter(nombre__icontains="termo")
```

busca productos cuyo nombre contenga la palabra "termo", sin distinguir entre mayúsculas y minúsculas

## 8 buscar productos de la categoría Hogar y Cocina

```python
Producto.objects.filter(categoria__nombre__icontains="hogar")
```

busca productos cuya categoría contenga la palabra "hogar". En este caso devuelve Termo, Cubiertos, Sarten y Set de Vasos

## 9 buscar productos con precio menor a 1000

```python
Producto.objects.filter(precio__lt=1000)
```

Busca productos cuyo precio sea menor a 1000

## 10 buscar productos mediante una lista de IDs

```python
Producto.objects.filter(id__in=[1, 2, 3])
```

Busca los productos cuyos IDs sean 1, 2 o 3

## consulta adicional: acceder a la categoría de un producto

```python
producto = Producto.objects.get(id=1)
producto.categoria.nombre
```

permite acceder desde un producto a su categoría. En este caso devuelve "Hogar y Cocina"

## crear un producto desde el shell

```python
categoria = Categoria.objects.first()

producto = Producto.objects.create(
    nombre="Termo Nuevo",
    marca="Stanley",
    descripcion="Termo de acero inoxidable",
    precio=5000,
    categoria=categoria
)
```

crea un nuevo producto y lo relaciona con una categoría
