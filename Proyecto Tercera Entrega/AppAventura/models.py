from django.db import models

# Create your models here.
class Articulos_camping(models.Model):
    tipo_articulo = models.CharField(max_length=20)
    marca = models.CharField(max_length=20)
    ano = models.IntegerField()

class Articulos_hidratación(models.Model):
    tipo_articulo = models.CharField(max_length=3)
    marca = models.CharField(max_length=3)
    litros = models.IntegerField()

class Articulos_alimentacion(models.Model):
    tipo_alimento = models.CharField(max_length=10)
    marca = models.CharField(max_length=4)

