from django.shortcuts import render


def home(request):
    return render(request, 'miapp/home.html')


def productos(request):
    return render(request, 'miapp/productos.html')


def acerca_de_mi(request):
    return render(request, 'miapp/acerca-de-mi.html')