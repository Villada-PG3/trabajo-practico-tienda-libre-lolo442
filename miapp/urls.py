from django.urls import path
from . import views
urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('productos/', views.productos, name='productos'),
    path('acerca-de-mi/', views.acerca_de_mi, name='acerca_de_mi'),
    path("catalogo/", views.CatalogoView.as_view(), name="catalogo"),
    path("producto/<int:pk>/", views.detalle_producto, name="detalle_producto"),

]