from django.contrib import admin
from .models import Usuario, Pedido, Categoria, Producto, Carrito, Stock

# Register your models here.

admin.site.register(Usuario)
admin.site.register(Pedido)
admin.site.register(Categoria)
admin.site.register(Producto)
admin.site.register(Carrito)
admin.site.register(Stock)