from pickle import TRUE
from django.db import models

# Create your models here.
class Productos(models.Model):
    nombre = models.CharField(max_length=200)
    sku = models.CharField(max_length=100, unique=True)
    marca = models.CharField(max_length=3)
    modelo = models.CharField(max_length=100)
    tipo = models.IntegerField()
    precio = models.FloatField()
    stock = models.IntegerField()
    descuento = models.FloatField()
    novedad = models.BooleanField()    
    imagen = models.CharField(max_length=100)
    def __str__(self):
        return self.nombre


class Marcas(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    def __str__(self):
        return self.nombre

class Tipo(models.Model):
    categoria = models.CharField(max_length=100, unique=True)
    def __str__(self):
        return self.categoria

class Distribuidores(models.Model):
    razon_social = models.CharField(max_length=200)
    direccion = models.CharField(max_length=100)
    localidad = models.CharField(max_length=100)
    pais = models.CharField(max_length=100)
    telefono = models.CharField(max_length=100)
    mail = models.CharField(max_length=100)
    web = models.CharField(max_length=100)
    cuit=models.IntegerField(unique=True)
    def __str__(self):
        return self.razon_social

class Distribuidores_Marcas(models.Model):
    marca = models.IntegerField()
    distribuidor = models.IntegerField()



