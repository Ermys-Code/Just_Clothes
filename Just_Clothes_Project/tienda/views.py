from django.shortcuts import render
from .models import Usuario, Pedido, Categoria, Producto, Carrito, Stock
from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import redirect

# Create your views here.


def main(request):
    
    
    context = {
    }
    
    return render(request, "main.html", context=context)

def filter(request):
    
    context = {
        
    }
    
    return render(request, "filter.html", context = context)
