from django.shortcuts import render
from .models import Usuario, Pedido, Categoria, Producto, Carrito, Stock
from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import redirect

# Create your views here.


def main(request):
    
    categories = []
    
    products = []
    
    
    
    for category in Categoria.objects.all():
        categories.append(category)
    
    for product in Producto.objects.all():
        products.append(product)
        
    
    
    
    context = {
    }
    
    return render(request, "main.html", context=context)

def filter(request):
    
    context = {
        
    }
    
    return render(request, "filter.html", context = context)
