from django.urls import path
from CRUD import views


urlpatterns = [
    path('index/', views.index, name='index'),
    path('productos/', views.productos, name='productos'),
    path('proveedor/', views.proveedores, name='proveedor'),
    path('soporte/', views.soporte, name='soporte'),
    path('usuarios/', views.usuarios, name='usuarios'),
]