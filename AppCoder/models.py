from django.db import models

# Create your models here.

class Viajero(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()
    profesion = models.CharField(max_length=30)

class Destino(models.Model):
    nombre = models.CharField(max_length=30)
    pais = models.CharField(max_length=30)

class Establecimiento(models.Model):
    nombre = models.CharField(max_length=30)
    rubro = models.CharField(max_length=30)
    calificacion = models.IntegerField()