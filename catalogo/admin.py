from django.contrib import admin
from .models import Producto, Categoria, Sede # <--- Agrega Sede aquí

admin.site.register(Producto)
admin.site.register(Categoria)
admin.site.register(Sede) # <--- Y regístralo aquí