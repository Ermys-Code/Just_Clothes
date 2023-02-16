from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path("", views.main, name= "main" ),
    path("filter", views.filter_global, name= "filter_global" ),
    path("filter/<int:pk>", views.filter_category, name="filter_category"),
    path("product/<int:pk>", views.detalle_producto, name="detalle_producto"),
]

