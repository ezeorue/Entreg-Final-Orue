from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, Context
from .models import *
from .forms import *
# Create your views here.

# Vista Inicio
def inicio(request):
    return render(request, 'Layout/index.html')
# Vista Inicio

# Vista y Métodos para Clientes

def cliente(request):
    clientes = Cliente.objects.all()
    contexto = {"clientes": clientes}
    return render(request, 'Clientes/index.html', contexto)

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
        d = request.GET['dni'] 
        clientes = Cliente.objects.filter(dni=d)
        if (clientes):
            return render(request, "Clientes/index.html", {"clientes":clientes})
        else:
            respuesta = "No se encontró nadie con ese DNI"
            return render(request, "Clientes/search.html", {"respuesta":respuesta})

    return render(request, 'Clientes/search.html')

# Vista y Métodos para Clientes

# Vista y Métodos para Autos

def auto(request):
    autos = Auto.objects.all()
    contexto = {"autos": autos}
    return render(request, 'Autos/index.html', contexto)

def autoAdd(request):
    if request.method == 'POST':
        miForm = AutoForm(request.POST)
        print(miForm)

        if miForm.is_valid:
            info = miForm.cleaned_data
            auto = Auto(patente = info['patente'],marca = info['marca'],modelo = info['modelo'])
            auto.save()
            return render(request, 'Layout/index.html')
    else:
        miForm = AutoForm()

    return render(request, 'Autos/add.html', {'miForm':miForm})

# Vista y Métodos para Autos

# Vista y Métodos para Historial

def historial(request):
    historial = Historial.objects.all()
    contexto = {"historial": historial}
    return render(request, 'Historial/index.html', contexto)

def historialAdd(request):
    if request.method == 'POST':
        miForm = HistorialForm(request.POST)
        print(miForm)

        if miForm.is_valid:
            info = miForm.cleaned_data
            historial = Historial(diagnostico = info['diagnostico'],reparacion = info['reparacion'])
            historial.save()
            return render(request, 'Layout/index.html')
    else:
        miForm = HistorialForm()

    return render(request, 'Historial/add.html', {'miForm':miForm})

# Vista y Métodos para Historial

# Vista y Métodos para Presupuesto
def presupuesto(request):
    presupuesto = Presupuesto.objects.all()
    contexto = {"presupuesto": presupuesto}
    return render(request, 'Presupuesto/index.html', contexto)

def presupuestoAdd(request):
    if request.method == 'POST':
        miForm = PresupuestoForm(request.POST)
        print(miForm)

        if miForm.is_valid:
            info = miForm.cleaned_data
            presupuesto = Presupuesto(detalle = info['detalle'],costo = info['costo'],fpago = info['fpago'],estado = info['estado'])
            presupuesto.save()
            return render(request, 'Layout/index.html')
    else:
        miForm = PresupuestoForm()

    return render(request, 'Presupuesto/add.html', {'miForm':miForm})

# Vista y Métodos para Presupuesto