from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('productos/', views.productos, name='productos'),
    path('acerca-de-mi/', views.acerca_de_mi, name='acerca_de_mi'),
    path("catalogo/", views.catalogo, name="catalogo"),
]