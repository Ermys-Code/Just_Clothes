from django.shortcuts import render
from .models import Usuario, Pedido, Categoria, Producto, Carrito, Stock
from .forms import EditProfile
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
    
    user = request.user
    just_clothes_user = None
    
    for usuario in Usuario.objects.all():
        if usuario.user == user:
            just_clothes_user = usuario
    
    carrito = Carrito()
    
    orders = Pedido.objects.filter(user_id__exact=just_clothes_user)
    
    if(len(orders) <= 0):
        pedido = Pedido()
        pedido.user_id = just_clothes_user
        pedido.save()
        
        carrito.order_id = pedido
        
    else:
        carrito.order_id = orders[0]
    
    carrito.price = product.price
    carrito.product_id = product
    carrito.cuantity = 1
    carrito.save()
    
    return redirect("detalle_producto", pk = product.id)


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

def buy(request, pk):
    order = Pedido.objects.get(pk=pk)
    
    carrito = Carrito.objects.filter(order_id__exact = order)
    
    for product in carrito:
        product.delete()
    
    return redirect("carrito")
    
    


def carrito(request):
    categories = []
    user = request.user
    just_clothes_user = None
    
    for category in Categoria.objects.all():
        categories.append(category)
    
    for usuario in Usuario.objects.all():
        if usuario.user == user:
            just_clothes_user = usuario
            
    orders = Pedido.objects.filter(user_id__exact=just_clothes_user)
    
    carrito = []
    order_contents = []
    
    if(len(orders) >= 0):
        order_contents = Carrito.objects.filter(order_id__exact = orders[0])
        
    for content in order_contents:
        
        product = content.product_id
        
        carrito.append(product)
        
    context = {
        "pedido":orders[0],
        "carrito":carrito,
        "categories":categories,
    }
    
    return render(request, "carrito.html", context = context)
    

def profile(request):    
    user = request.user
    just_clothes_user = None
    
    categories = []
    
    for category in Categoria.objects.all():
        categories.append(category)
    
    for usuario in Usuario.objects.all():
        if usuario.user == user:
            just_clothes_user = usuario
            
    
    username = just_clothes_user.user.username
    first_name = just_clothes_user.user.first_name
    last_name = just_clothes_user.user.last_name
    email = just_clothes_user.user.email
    address = just_clothes_user.address
    
    sent = False
    message = ""
    if request.method == "POST":
        form = EditProfile(request.POST)
        if form.is_valid():
            try:
                just_clothes_user.user.username = form.cleaned_data["username"]
                just_clothes_user.user.first_name = form.cleaned_data["first_name"]
                just_clothes_user.user.last_name = form.cleaned_data["last_name"]
                just_clothes_user.user.email = form.cleaned_data["email"]
                just_clothes_user.address = form.cleaned_data["address"]
                just_clothes_user.save()
                sent = True
                form = EditProfile()
            except:
                message = "Error saving values"
        else:
            message = "Values not valid"
    else:
        form = EditProfile()
        
    
    context = {
        "categories" : categories,
        "username" : username,
        "first_name" : first_name,
        "last_name" : last_name,
        "email" : email,
        "address" : address,
        "form" : form,
        "message" : message,
        "sent" : sent,
    }
    
    return render(request, "profile.html", context=context)