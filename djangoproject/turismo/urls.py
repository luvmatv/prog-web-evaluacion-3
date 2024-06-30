from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  
    path('productos/', views.producto_lista, name='producto_lista'),
    path('productos/<int:pk>/', views.producto_detalle, name='producto_detalle'),
    path('productos/nuevo/', views.producto_crear, name='producto_crear'),
    path('productos/editar/<int:pk>/', views.producto_editar, name='producto_editar'),
    path('productos/eliminar/<int:pk>/', views.producto_eliminar, name='producto_eliminar'),
    path('carrito/', views.carrito_lista, name='carrito_lista'),
    path('carrito/agregar/', views.carrito_agregar, name='carrito_agregar'),
    path('carrito/editar/<int:pk>/', views.carrito_editar, name='carrito_editar'),
    path('carrito/eliminar/<int:pk>/', views.carrito_eliminar, name='carrito_eliminar'),
]
