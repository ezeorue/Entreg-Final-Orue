from django.shortcuts import render

from django.template import RequestContext

def inicio(request):
    return render(request, 'Layout/index.html')

def aboutme(request):
    return render(request, 'Layout/about.html')