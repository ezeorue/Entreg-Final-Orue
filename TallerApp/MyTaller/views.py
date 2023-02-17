from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, Context
from .models import *

# Create your views here.

def inicio(request):
    return render(request, 'Layout/default.html')

def cliente(request):
    return render(request, 'Clientes/index.html')
    
def auto(request):
    return render(request, 'Autos/index.html')

def historial(request):
    return render(request, 'Historial/index.html')

def presupuesto(request):
    return render(request, 'Presupuesto/index.html')