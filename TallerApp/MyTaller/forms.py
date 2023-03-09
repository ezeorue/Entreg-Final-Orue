from django import forms

class ClienteForm(forms.Form):
    nombre = forms.CharField(max_length=100)
    apellido = forms.CharField(max_length=100)
    dni = forms.CharField(max_length=12)
    celular = forms.CharField(max_length=50)
    mail = forms.CharField(max_length=150)

class AutoForm(forms.Form):
    patente = forms.CharField(max_length=20)
    marca = forms.CharField(max_length=50)
    modelo = forms.CharField(max_length=150)

class HistorialForm(forms.Form):
    diagnostico = forms.CharField(max_length=255)
    reparacion = forms.CharField(max_length=255)

class PresupuestoForm(forms.Form):
    detalle = forms.CharField(max_length=255)
    costo = forms.CharField(max_length=255)
    fpago = forms.CharField(max_length=25)
    estado = forms.BooleanField(required=False,initial=False)

class RegistrarMecanico(forms.Form):
    nombre = forms.CharField(label="Nombre", max_length=100)
    apellido = forms.CharField(label="Apellido", max_length=100)
    nacimiento = forms.DateField()
    mail = forms.CharField(label="E-Mail", max_length=100)
    password = forms.CharField(label="Password",max_length=100)