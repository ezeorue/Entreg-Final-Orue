from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, Context
from MyTaller.models import *
from MyTaller.forms import *
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
# Create your views here.

class AutoList(ListView):
    model = Auto
    template_name = "Autos/index.html"

class AutoAdd(CreateView):
    model = Auto
    template_name = "Autos/add.html"
    success_url = "/autos/listar"
    fields = ['marca', 'patente', 'modelo']

class AutoView(DetailView):
    model = Auto
    template_name = "Autos/view.html"

class AutoEdit(UpdateView):
    model = Auto
    template_name = "Autos/edit.html"
    success_url = "/autos/listar"
    fields = ['marca', 'patente', 'modelo']

class AutoDelete(DeleteView):
    model = Auto
    template_name = "Autos/delete.html"
    success_url = "/autos/listar"