from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, Context
from .models import *
from .forms import *
# Create your views here.

def inicio(request):
    return render(request, 'Layout/index.html')

def cliente(request):
    clientes = Cliente.objects.all()
    contexto = {"clientes": clientes}
    return render(request, 'Clientes/index.html', contexto)

"""
def clienteAdd(request):
    if request.method == 'POST':
        cliente = Cliente(nombre = request.POST['nombre'],apellido = request.POST['apellido'],dni = request.POST['dni'],celular = request.POST['celular'],mail = request.POST['mail'])
        cliente.save()
        return render(request, 'Layout/index.html')
    return render(request, 'Clientes/add.html')
"""

def clienteAdd(request):
    if request.method == 'POST':
        miForm = ClienteForm(request.POST)
        print(miForm)

        if miForm.is_valid:
            info = miForm.cleaned_data
            cliente = Cliente(nombre = info['nombre'],apellido = info['apellido'],dni = info['dni'],celular = info['celular'],mail = info['mail'])
            cliente.save()
            return render(request, 'Layout/index.html')
    else:
        miForm = ClienteForm()

    return render(request, 'Clientes/add.html', {'miForm':miForm})

def clienteSearch(request):
    if  request.method == 'GET' and 'dni' in request.GET:
        dni = request.GET['dni'] 
        clientes = Cliente.objects.filter(dni__icontains=dni)
        return render(request, "Clientes/index.html", {"clientes":clientes})
    else: 
        respuesta = "No enviaste datos"

    return render(request, 'Clientes/search.html')

def auto(request):
    return render(request, 'Autos/index.html')

def historial(request):
    return render(request, 'Historial/index.html')

def presupuesto(request):
    return render(request, 'Presupuesto/index.html')