from django.contrib import admin
from .models import Productos, Proveedor, Pasillo

#registrar modelo de tabla
admin.site.register(Productos)
admin.site.register(Proveedor)
admin.site.register(Pasillo)