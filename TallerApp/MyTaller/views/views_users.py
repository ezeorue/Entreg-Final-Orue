from django.shortcuts import render, redirect
from django.http import HttpResponse
from MyTaller.forms import UserRegisterForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from MyTaller.forms import *
from django.contrib.auth.hashers import make_password

def registro(request):
    form = UserRegisterForm(request.POST)
    if request.method == 'POST':
        
        if form.is_valid():
            form.save() 
            return redirect("Registro")
    
        else:
            return render(request, "Mecanicos/register.html", {'form': form})
    
    form = UserRegisterForm()
    return render(request, 'Mecanicos/register.html', {'form':form})

def login_request(request):

    if request.method == "POST":
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():
            usr = form.cleaned_data.get('username')
            passw = form.cleaned_data.get('password')

            user = authenticate(username=usr, password=passw)

            if user is not None:
                login(request, user)
                return render(request, 'Layout/index.html')
            else:
                return render(request, "Layout/login.html", {"form":form, "msg":"Usuario o Password incorrecta."})
        else:
            return render(request, "Layout/login.html", {"form":form, "msg":"Usuario o Password incorrecta."})
        
    form = AuthenticationForm()
    return render(request,"Layout/login.html", {"form":form})

def userEdit(request):

    usuario = request.user
    if request.method =="POST":
        form = UserEditForm(request.POST)
        if form.is_valid():
            datos = form.cleaned_data
            usuario.first_name = datos["first_name"]
            usuario.last_name = datos["last_name"]
            usuario.email = datos["email"]
            usuario.save()
            user = authenticate(username=usuario.username, password=usuario.password)
            return redirect("Inicio")
    
    else:
        form = UserEditForm(initial={"first_name":usuario.first_name, "last_name":usuario.last_name, "email":usuario.email})
    

    context = {"form":form, "usuario":usuario}
    return render(request, "Mecanicos/edit.html", context)