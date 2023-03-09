from django.db import models

class Mecanicos(models.Model):
    user = models.CharField(max_length=100)
    mail = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)

    def __str__(self):
        return f"ID {self.id} - Nombre: {self.nombre} - Apellido: {self.apellido}"
    
class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    dni = models.CharField(max_length=12)
    celular = models.CharField(max_length=50)
    mail = models.EmailField(max_length=150)

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
    ABONADO='1'
    IMPAGO='0'

    ESTADO = [
        (ABONADO, 'Abonado'),
        (IMPAGO, 'Impago'),
    ]

    DEBITO='0'
    CREDITO='1'
    TRANSFERENCIA='2'
    EFECTIVO='3'

    FPAGO = [
        (DEBITO, 'Débito'),
        (CREDITO, 'Crédito'),
        (TRANSFERENCIA, 'Transferencia'),
        (EFECTIVO, 'Efectivo'),
    ]

    detalle = models.CharField(max_length=255)
    costo = models.FloatField()
    fpago = models.CharField(
        max_length=2,
        choices=FPAGO,
        )
    estado = models.CharField(
        max_length=2,
        choices=ESTADO,
        )

    def __str__(self):
        return f"ID {self.id} - Detalle: {self.detalle}"