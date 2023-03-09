from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, Context
from MyTaller.models import *
from MyTaller.forms import *
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
# Create your views here.

class PresupuestoList(ListView):
    model = Presupuesto
    template_name = "Presupuesto/index.html"

class PresupuestoAdd(CreateView):
    model = Presupuesto
    template_name = "Presupuesto/add.html"
    success_url = "/presupuesto/listar"
    fields = ['detalle', 'costo', 'fpago', 'estado']

class PresupuestoEdit(UpdateView):
    model = Presupuesto
    template_name = "Presupuesto/edit.html"
    success_url = "/presupuesto/listar"
    fields = ['detalle', 'costo', 'fpago', 'estado']

class PresupuestoDelete(DeleteView):
    model = Presupuesto
    template_name = "Presupuesto/delete.html"
    success_url = "/presupuesto/listar"