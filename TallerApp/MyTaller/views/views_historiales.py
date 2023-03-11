from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, Context
from MyTaller.models import *
from MyTaller.forms import *
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
# Create your views here.

class HistorialList(ListView):
    model = Historial
    template_name = "Historial/index.html"

class HistorialAdd(CreateView):
    model = Historial
    template_name = "Historial/add.html"
    success_url = "/historial/listar"
    fields = ['diagnostico', 'reparacion']

class HistorialView(DetailView):
    model = Historial
    template_name = "Historial/view.html"

class HistorialEdit(UpdateView):
    model = Historial
    template_name = "Historial/edit.html"
    success_url = "/historial/listar"
    fields = ['diagnostico', 'reparacion']

class HistorialDelete(DeleteView):
    model = Historial
    template_name = "Historial/delete.html"
    success_url = "/historial/listar"