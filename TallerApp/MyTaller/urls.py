from django.urls import path
from MyTaller.views.views_clientes import *
from MyTaller.views.views_autos import *
from MyTaller.views.views_historiales import *
from MyTaller.views.views_presupuestos import *
from MyTaller.views.views_mecanicos import *
from MyTaller.views.views import *

urlpatterns = [
    path('', inicio, name="Inicio"),
    path('aboutme', aboutme, name="Aboutme"),
    path('clientes/listar', ClienteList.as_view(), name='Clientes'),
    path('cliente/'r'<pk>', ClienteView.as_view(), name="ClienteView"),
    path('cliente/add/', ClienteAdd.as_view(), name="ClienteAdd"),
    path('cliente/edit/'r'<pk>', ClienteEdit.as_view(), name="ClienteEdit"),
    path('cliente/delete/'r'<pk>', ClienteDelete.as_view(), name="ClienteDelete"),
    path('search-cliente/', clienteSearch, name="clienteSearch"),
    path('autos/listar', AutoList.as_view(), name='Autos'),
    path('auto/add/', AutoAdd.as_view(), name="AutoAdd"),
    path('auto/edit/'r'<pk>', AutoEdit.as_view(), name="AutoEdit"),
    path('auto/delete/'r'<pk>', AutoDelete.as_view(), name="AutoDelete"),
    path('historial/listar', HistorialList.as_view(), name='Historiales'),
    path('historial/add/', HistorialAdd.as_view(), name="HistorialAdd"),
    path('historial/edit/'r'<pk>', HistorialEdit.as_view(), name="HistorialEdit"),
    path('historial/delete/'r'<pk>', HistorialDelete.as_view(), name="HistorialDelete"),
    path('presupuesto/listar', PresupuestoList.as_view(), name='Presupuestos'),
    path('presupuesto/add/', PresupuestoAdd.as_view(), name="PresupuestoAdd"),
    path('presupuesto/edit/'r'<pk>', PresupuestoEdit.as_view(), name="PresupuestoEdit"),
    path('presupuesto/delete/'r'<pk>', PresupuestoDelete.as_view(), name="PresupuestoDelete"),
    path('mecanico/listar', MecanicoList.as_view(), name="Mecanicos"),
    path('mecanico/registrar', MecanicoRegister.as_view(), name="MecanicoRegister"),
]