from django.db import models
from django.urls import reverse

# Create your models here.


class Usuario(models.Model):
    user = models.OneToOneField("auth.user", on_delete=models.CASCADE)
    address=models.CharField('address',max_length=200,null=False)



class Pedido(models.Model):
    user_id = models.ForeignKey('Usuario',on_delete=models.SET_NULL,null=True,blank=True)

    def get_absolute_url(self):
        return reverse('buy',args=[str(self.id)])



class Categoria(models.Model):
    name=models.CharField('name',max_length=200,null=False)
    
    def get_absolute_url(self):
        return reverse('filter_category',args=[str(self.id)])
    
    def __str__(self):
        return self.name

class Producto(models.Model):
    name=models.CharField('name',max_length=200,null=False)
    description = models.CharField('description', max_length=2000, null=False)
    category = models.ForeignKey('Categoria',on_delete=models.SET_NULL,null=True,blank=True)
    img = models.ImageField(upload_to='images/', default=None)
    size=models.CharField('size',max_length=200,null=False)
    color=models.CharField('color',max_length=200,null=False)
    price=models.FloatField(null=False, default=0)

    def get_absolute_url(self):
        return reverse('detalle_producto',args=[str(self.id)])
    
    def get_absolute_url_add_to_cart(self):
        return reverse('add_to_cart',args=[str(self.id)])

    def get_absolute_url_delete_to_cart(self):
        return reverse('delete_to_cart',args=[str(self.id)])

    def __str__(self):
        return self.name

class Carrito(models.Model):
    order_id=models.ForeignKey('Pedido',on_delete=models.SET_NULL,null=True,blank=True)
    product_id=models.ForeignKey('Producto',on_delete=models.SET_NULL,null=True,blank=True)
    cuantity=models.IntegerField(null=False)
    price=models.FloatField(null=False)

    def __str__(self):
        return str(self.id)


class Stock(models.Model):
    product_id=models.ForeignKey('Producto',on_delete=models.SET_NULL,null=True,blank=True)
    cuantity=models.IntegerField(null=False)

    def __str__(self):
        return str(self.id)




