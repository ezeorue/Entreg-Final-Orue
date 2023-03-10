from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, Context
from MyTaller.models import *
from MyTaller.forms import *
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
# Create your views here.

class MecanicoList(ListView):
    model = Mecanico
    template_name = "Mecanico/index.html"

class MecanicoRegister(CreateView):
    model = Mecanico
    template_name = "Mecanico/register.html"
    success_url = "/mecanico/listar"
    fields = ['detalle', 'costo', 'fpago', 'estado']
