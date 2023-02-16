from django.db import models
from django.urls import reverse

# Create your models here.


class Usuario(models.Model):
    user = models.OneToOneField("auth.user", on_delete=models.CASCADE)
    address=models.CharField('address',max_length=200,null=False)

    def __str__(self):
        return self.titulo


class Pedido(models.Model):
    user_id = models.ForeignKey('Usuario',on_delete=models.SET_NULL,null=True,blank=True)

    def __str__(self):
        return self.user_id

    def get_absolute_url(self):
        return reverse('mostrar_carrito',args=[str(self.id)])



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

    def __str__(self):
        return self.name

class Carrito(models.Model):
    order_id=models.ForeignKey('Pedido',on_delete=models.SET_NULL,null=True,blank=True)
    product_id=models.ForeignKey('Producto',on_delete=models.SET_NULL,null=True,blank=True)
    cuantity=models.IntegerField(null=False)
    price=models.FloatField(null=False)

    def __str__(self):
        return self.id


class Stock(models.Model):
    product_id=models.ForeignKey('Producto',on_delete=models.SET_NULL,null=True,blank=True)
    cuantity=models.IntegerField(null=False)

    def __str__(self):
        return self.id




