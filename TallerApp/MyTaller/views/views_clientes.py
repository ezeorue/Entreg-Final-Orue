from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, Context
from MyTaller.models import *
from MyTaller.forms import *
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
# Create your views here.

class ClienteList(ListView):
    model = Cliente
    template_name = "Clientes/index.html"

class ClienteAdd(CreateView):
    model = Cliente
    template_name = "Clientes/add.html"
    success_url = "/clientes/listar"
    fields = ['nombre', 'apellido', 'dni', 'celular', 'mail']

class ClienteView(DetailView):
    model = Cliente
    template_name = "Clientes/view.html"

class ClienteEdit(UpdateView):
    model = Cliente
    template_name = "Clientes/edit.html"
    success_url = "/clientes/listar"
    fields = ['nombre', 'apellido', 'dni', 'celular', 'mail']

class ClienteDelete(DeleteView):
    model = Cliente
    template_name = "Clientes/delete.html"
    success_url = "/clientes/listar"

def clienteSearch(request):
    if  request.method == 'GET' and 'dni' in request.GET:
        d = request.GET['dni'] 
        clientes = Cliente.objects.filter(dni=d)
        if (clientes):
            return render(request, "Clientes/index.html", {"object_list":clientes})
        else:
            respuesta = "No se encontró nadie con ese DNI"
            return render(request, "Clientes/search.html", {"respuesta":respuesta})

    return render(request, 'Clientes/search.html')