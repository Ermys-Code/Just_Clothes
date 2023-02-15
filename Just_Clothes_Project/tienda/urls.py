from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path("", views.main, name= "main" ),
    path("", views.filter_global, name= "filter_global" ),
    path("category/<int:pk>", views.filter_category, name="filter_category"),
]

