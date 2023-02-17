from django.shortcuts import render
from .models import Usuario, Pedido, Categoria, Producto, Carrito, Stock
from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import redirect

# Create your views here.


def main(request):
    products = []
    categories = []
    
    
    for category in Categoria.objects.all():
        categories.append(category)
        provitional_list = Producto.objects.filter(category__exact=category) 
        products.append(provitional_list)
    
    
    context = {
        "products":products,
         "categories":categories,
    }
    
    return render(request, "main.html", context=context)
    

def filter_global(request):
    
    results = []
    categories = []
    
    applied = request.POST
    
    for category in Categoria.objects.all():
        categories.append(category)
        
    for product in Producto.objects.all():
        if(applied.get("search") in product.name or applied.get("search") in product.description or applied.get("search") == product.category or applied.get("search") == product.color):
            results.append(product)
                      
    context = {
        "applied":applied.get("search"),
         "categories":categories,
        "results":results,
            
    }
    
    return render(request, "filter.html", context = context)

def filter_category(request, pk):
    
    categories = []
    
    for category in Categoria.objects.all():
        categories.append(category)
    
    applied = Categoria.objects.get(pk=pk)
    
    results = Producto.objects.filter(category__exact=applied) 
        
    context = {
        "applied":applied,
         "categories":categories,
        "results":results,
    }
    
    return render(request, "filter.html", context = context)

def add_to_cart(request, pk):
    product = Producto.objects.get(pk=pk)
    user = request.Usuario
    carrito = Carrito()
    
    orders = Pedido.objects.filter(user_id__exact=user)
    
    if(orders <= 0):
        pedido = Pedido()
        pedido.user_id = user
        pedido.save()
        
        carrito.order_id = pedido.id
        
    else:
        carrito.order_id = orders[0].id
    
    carrito.price = product.price
    carrito.product_id = product.id
    carrito.cuantity = 1
    
    return redirect(product.get_absolute_url)


def detalle_producto(request, pk):
    categories = []
    
    for category in Categoria.objects.all():
        categories.append(category)
    
    product = Producto.objects.get(pk=pk) 
    
    context = {
        "product":product,
        "categories":categories,
    }
    
    return render(request, "detalle_producto.html", context = context)




def profile(request):    
    user = request.user
    username = request.user.username
    first_name = request.user.first_name
    last_name = request.user.last_name
    email = request.user.email
    
    sent = False
    message = ""
    if request.method == "POST":
        form = EditProfile(request.POST)
        if form.is_valid():
            try:
                user.username = form.cleaned_data["username"]
                user.first_name = form.cleaned_data["first_name"]
                user.last_name = form.cleaned_data["last_name"]
                user.email = form.cleaned_data["email"]
                user.save()
                sent = True
                form = EditProfile()
            except:
                message = "Error saving values"
        else:
            message = "Values not valid"
    else:
        form = EditProfile()
        
    
    context = {
        "username" : username,
        "first_name" : first_name,
        "last_name" : last_name,
        "email" : email,
        "form" : form,
        "message" : message,
        "sent" : sent,
    }
    
    return render(request, "profile.html", context=context)