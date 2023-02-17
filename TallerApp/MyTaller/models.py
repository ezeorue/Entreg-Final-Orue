from django.db import models

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    dni = models.CharField(max_length=12)
    celular = models.CharField(max_length=50)
    mail = models.CharField(max_length=150)

    def __str__(self):
        return f"ID {self.id} - Nombre: {self.nombre} - Apellido: {self.apellido} - DNI: {self.dni} - Celular: {self.celular} - Mail: {self.mail}"

class Auto(models.Model):
    patente = models.CharField(max_length=20)
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=150)

    def __str__(self):
        return f"ID {self.id} - Patente: {self.patente} - Marca: {self.marca}"

class Historial(models.Model):
    diagnostico = models.CharField(max_length=255)
    reparacion = models.CharField(max_length=255)

    def __str__(self):
        return f"ID {self.id} - Diagnostico: {self.diagnostico}"

class Presupuesto(models.Model):
    detalle = models.CharField(max_length=255)
    costo = models.FloatField()
    fpago = models.CharField(max_length=25)
    estado = models.BooleanField(default=False)

    def __str__(self):
        return f"ID {self.id} - Detalle: {self.detalle}"