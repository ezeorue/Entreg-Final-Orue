from django.urls import path
from MyTaller.views import *

urlpatterns = [
    path('', inicio, name="Inicio"),
    path('clientes/', cliente),
    path('autos/', auto),
    path('historiales/', historial),
    path('presupuestos/', presupuesto),
]
