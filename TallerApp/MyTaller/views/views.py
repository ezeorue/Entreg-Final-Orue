from django.shortcuts import render

# Vista Inicio
def inicio(request):
    return render(request, 'Layout/index.html')

def aboutme(request):
    return render(request, 'Layout/about.html')