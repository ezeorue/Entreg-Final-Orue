from django.urls import path
from MyTaller.views import *

urlpatterns = [
    path('', inicio, name="Inicio"),
    path('clientes/', cliente, name="Clientes"),
    path('add-cliente/', clienteAdd, name="clienteAdd"),
    path('search-cliente/', clienteSearch, name="clienteSearch"),
    path('autos/', auto, name="Autos"),
    path('historiales/', historial, name="Historiales"),
    path('presupuestos/', presupuesto, name="Presupuestos"),
]
