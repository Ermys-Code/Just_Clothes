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
        provitional_list = Producto.objects.filter(category__exact=category) 
        products.append(provitional_list)
    
    
    context = {
        "categories":categories,
        "products":products,
    }
    
    return render(request, "main.html", context=context)

def filter_global(request):
    
    results = []
    
    applied = request.POST
        
    for product in Producto.objects.all():
        if(applied in product.name or applied in product.description or applied == product.category or applied == product.color):
            results.append(product)
                      
    context = {
        
        "results":results
            
    }
    
    return render(request, "filter.html", context = context)

def filter_category(request, pk):
    
    applied = Categoria.objects.get(pk=pk)
    
    results = Producto.objects.filter(category__exact=applied) 
        
    context = {
        
        "results":results
    }
    
    return render(request, "filter.html", context = context)