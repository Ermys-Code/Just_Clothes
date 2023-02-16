from django.shortcuts import render
from .models import Usuario, Pedido, Categoria, Producto, Carrito, Stock
from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import redirect

# Create your views here.


def main(request):
    
    products = []
    
    
    for category in Categoria.objects.all():
        provitional_list = Producto.objects.filter(category__exact=category) 
        products.append(provitional_list)
    
    
    context = {
        "products":products,
    }
    
    return render(request, "main.html", context=context)

def base_generic(request):
    
    categories = []
    for category in Categoria.objects.all():
        categories.append(category)
        
    context = {
        "categories":categories,
    }
    
    return render(request, "base_generic.html", context=context)
    

def filter_global(request):
    
    results = []
    
    applied = request.POST
        
    for product in Producto.objects.all():
        if(applied.get("search") in product.name or applied.get("search") in product.description or applied.get("search") == product.category or applied.get("search") == product.color):
            results.append(product)
                      
    context = {
        "applied":applied.get("search"),
        
        "results":results
            
    }
    
    return render(request, "filter.html", context = context)

def filter_category(request, pk):
    
    applied = Categoria.objects.get(pk=pk)
    
    results = Producto.objects.filter(category__exact=applied) 
        
    context = {
        "applied":applied,
        
        "results":results
    }
    
    return render(request, "filter.html", context = context)

def addToCart(request, pk):
    product = Producto.objects.get(pk=pk)
    user = request.Usuario
    carrito = Carrito()
    
    if(Pedido.objects.filter(user_id__exact=user) <= 0):
        pedido = Pedido()
        pedido.user_id = user
        pedido.save()
        
        carrito.order_id = pedido.id
    
    carrito.price = product.price
    carrito.product_id = product.id
    carrito.cuantity = 1
    
    return redirect('detalle_producto')


def detalle_producto(request, pk):
    
    product = Producto.objects.get(pk=pk)
    
    
    context = {
        "product":product,
    }
    
    return render(request, "detalle_producto.html", context = context)